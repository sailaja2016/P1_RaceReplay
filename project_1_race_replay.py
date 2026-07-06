"""
Project 1: The Race Replay 🏁
F1 Race Visualization using FastF1 API and Matplotlib

This script fetches F1 race data and creates a 2D visualization of:
- Track layout
- Car positions throughout the race
- Driver information (number, team color)
"""

import fastf1
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd
from matplotlib.collections import LineCollection

# Enable FastF1 cache to speed up data loading
fastf1.Cache.enable_cache('E:/K.Sailaja/Project_1_Race_Replay/fastf1_cache')

class F1RaceReplay:
    def __init__(self, year, round_num, session_name='R'):
        """
        Initialize the Race Replay
        
        Args:
            year (int): Season year (e.g., 2024)
            round_num (int): Round number (1-24)
            session_name (str): 'FP1', 'FP2', 'FP3', 'Q', 'R' (Race)
        """
        self.year = year
        self.round_num = round_num
        self.session_name = session_name
        self.session = None
        self.laps = None
        self.track_info = None
        
    def load_session(self):
        """Load F1 session data from FastF1"""
        print(f"Loading {self.year} Round {self.round_num} ({self.session_name})...")
        try:
            self.session = fastf1.get_session(self.year, self.round_num, self.session_name)
            self.session.load()
            print(f"✓ Session loaded: {self.session.event['EventName']}")
            print(f"  Circuit: {self.session.event['Location']}")
            return True
        except Exception as e:
            print(f"✗ Error loading session: {e}")
            return False
    
    def get_track_coordinates(self):
        """Extract track layout from telemetry data"""
        print("Extracting track layout...")
        
        # Get one lap from the fastest driver to get track coordinates
        fastest_lap = self.session.laps.pick_fastest()
        
        if fastest_lap.telemetry is None or len(fastest_lap.telemetry) == 0:
            print("✗ No telemetry data available")
            return None
        
        telemetry = fastest_lap.telemetry
        x = telemetry['X'].values
        y = telemetry['Y'].values
        
        return np.column_stack([x, y])
    
    def plot_track(self, ax):
        """Draw the F1 track on the plot"""
        track_coords = self.get_track_coordinates()
        
        if track_coords is None:
            return
        
        # Plot track outline
        ax.plot(track_coords[:, 0], track_coords[:, 1], 'k-', linewidth=2, label='Track')
        ax.fill(track_coords[:, 0], track_coords[:, 1], color='green', alpha=0.1)
        
        # Add start/finish line
        ax.plot(track_coords[0, 0], track_coords[0, 1], 'r*', markersize=20, label='Start/Finish')
        
        return track_coords
    
    def get_driver_color(self, driver_number):
        """Get team color for a driver"""
        team_colors = {
            '1': '#DC0000',   # Ferrari Red
            '2': '#0082FA',   # Alpine Blue
            '3': '#FF8700',   # McLaren Orange
            '4': '#0000FF',   # Sauber Blue
            '14': '#B6BAFF',  # Alpine
            '16': '#C92D4B',  # Alfa Romeo
            '18': '#B6BAFF',  # Williams
            '20': '#C8082F',  # Haas Red
            '22': '#FF8700',  # McLaren
            '24': '#DC0000',  # Ferrari
            '27': '#00D2BE',  # Aston Martin
            '31': '#0082FA',  # Alpine
            '33': '#0000FF',  # Sauber
            '44': '#00D2BE',  # Mercedes
            '55': '#00D2BE',  # Mercedes
            '63': '#FF87BC',  # Mercedes (Guest)
            '77': '#0082FA',  # Alpine
            '81': '#0000FF',  # Sauber
        }
        return team_colors.get(str(int(driver_number)), '#808080')
    
    def visualize_race_snapshot(self, lap_num=10):
        """
        Create a static visualization of cars at a specific lap
        
        Args:
            lap_num (int): Lap number to visualize
        """
        if self.session is None:
            self.load_session()
        
        fig, ax = plt.subplots(figsize=(14, 10))
        fig.suptitle(f'{self.session.event["EventName"]} - Lap {lap_num}', fontsize=16, fontweight='bold')
        
        # Plot track
        track_coords = self.plot_track(ax)
        
        if track_coords is None:
            print("Cannot visualize without track data")
            return
        
        # Get cars data for specific lap
        laps_data = self.session.laps[self.session.laps['LapNumber'] == lap_num]
        
        if len(laps_data) == 0:
            print(f"No data for lap {lap_num}")
            return
        
        # Plot each driver's position
        for idx, lap in laps_data.iterrows():
            telemetry = lap.telemetry
            
            if telemetry is None or len(telemetry) == 0:
                continue
            
            # Get current position (last point in telemetry)
            x = telemetry['X'].iloc[-1]
            y = telemetry['Y'].iloc[-1]
            
            driver_num = lap['DriverNumber']
            driver_abbr = lap['Driver']
            
            color = self.get_driver_color(driver_num)
            
            # Plot car position
            ax.scatter(x, y, s=300, c=color, edgecolors='black', linewidth=2, zorder=10)
            ax.text(x, y-100, f"{driver_abbr}\n#{int(driver_num)}", 
                   ha='center', fontsize=8, fontweight='bold')
        
        ax.set_xlabel('X Position (m)', fontsize=12)
        ax.set_ylabel('Y Position (m)', fontsize=12)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        ax.legend(loc='upper right')
        
        plt.tight_layout()
        return fig
    
    def visualize_positions_multiple_laps(self, lap_numbers=[5, 10, 20, 30]):
        """
        Create a grid showing race progress at multiple laps
        
        Args:
            lap_numbers (list): List of lap numbers to display
        """
        if self.session is None:
            self.load_session()
        
        num_subplots = len(lap_numbers)
        cols = 2
        rows = (num_subplots + cols - 1) // cols
        
        fig, axes = plt.subplots(rows, cols, figsize=(16, 12))
        axes = axes.flatten()
        
        fig.suptitle(f'{self.session.event["EventName"]} - Race Progression', 
                    fontsize=16, fontweight='bold')
        
        track_coords = self.get_track_coordinates()
        
        for idx, lap_num in enumerate(lap_numbers):
            ax = axes[idx]
            
            # Plot track
            if track_coords is not None:
                ax.plot(track_coords[:, 0], track_coords[:, 1], 'k-', linewidth=1.5)
                ax.fill(track_coords[:, 0], track_coords[:, 1], color='green', alpha=0.05)
            
            # Get lap data
            laps_data = self.session.laps[self.session.laps['LapNumber'] == lap_num]
            
            if len(laps_data) == 0:
                ax.text(0.5, 0.5, f'No data for Lap {lap_num}', 
                       ha='center', va='center', transform=ax.transAxes)
                ax.set_title(f'Lap {lap_num}', fontsize=12, fontweight='bold')
                continue
            
            # Plot positions
            for pos, (idx_row, lap) in enumerate(laps_data.iterrows(), 1):
                telemetry = lap.telemetry
                
                if telemetry is None or len(telemetry) == 0:
                    continue
                
                x = telemetry['X'].iloc[-1]
                y = telemetry['Y'].iloc[-1]
                driver_abbr = lap['Driver']
                color = self.get_driver_color(lap['DriverNumber'])
                
                ax.scatter(x, y, s=250, c=color, edgecolors='black', linewidth=1.5, zorder=10)
                ax.text(x, y-80, driver_abbr, ha='center', fontsize=7, fontweight='bold')
            
            ax.set_aspect('equal')
            ax.grid(True, alpha=0.2)
            ax.set_title(f'Lap {lap_num}', fontsize=12, fontweight='bold')
            ax.set_xlabel('X (m)', fontsize=9)
            ax.set_ylabel('Y (m)', fontsize=9)
        
        # Hide empty subplots
        for idx in range(num_subplots, len(axes)):
            axes[idx].set_visible(False)
        
        plt.tight_layout()
        return fig
    
    def get_lap_stats(self):
        """Get race statistics"""
        if self.session is None:
            return None
        
        print("\n" + "="*60)
        print(f"RACE STATISTICS: {self.session.event['EventName']}")
        print("="*60)
        
        # Get results
        results = self.session.results.sort_values('Points', ascending=False)
        
        print("\nTop 10 Finishers:")
        for idx, (_, driver) in enumerate(results.head(10).iterrows(), 1):
            print(f"{idx:2d}. {driver['Abbreviation']} - "
                  f"Team: {driver['TeamName']:20s} - "
                  f"Points: {driver['Points']}")
        
        return results


def main():
    """Main execution"""
    print("\n" + "="*60)
    print("PROJECT 1: F1 RACE REPLAY 🏁")
    print("="*60 + "\n")
    
    # Configuration: Change these to view different races
    YEAR = 2024
    ROUND = 6  # Spanish GP 2024
    SESSION = 'R'  # 'R' for Race, 'Q' for Quali, 'FP1' for FP1, etc.
    
    # Create replay object
    replay = F1RaceReplay(year=YEAR, round_num=ROUND, session_name=SESSION)
    
    # Load session data
    if not replay.load_session():
        print("Failed to load session. Check your internet connection.")
        return
    
    # Get race statistics
    replay.get_lap_stats()
    
    # Visualize specific lap
    print("\n📊 Creating visualization of Lap 10...")
    fig1 = replay.visualize_race_snapshot(lap_num=10)
    if fig1:
        plt.savefig('E:/K.Sailaja/Project_1_Race_Replay/outputs/race_replay_lap_10.png', dpi=150, bbox_inches='tight')
        print("✓ Saved: race_replay_lap_10.png")
        plt.show()
    
    # Visualize race progression
    print("\n📊 Creating race progression visualization...")
    fig2 = replay.visualize_positions_multiple_laps(lap_numbers=[5, 15, 25, 35])
    if fig2:
        plt.savefig('E:/K.Sailaja/Project_1_Race_Replay/outputs/race_progression.png', dpi=150, bbox_inches='tight')
        print("✓ Saved: race_progression.png")
        plt.show()
    
    print("\n" + "="*60)
    print("✓ Project 1 Complete!")
    print("="*60)
    print("\nNext Steps:")
    print("1. Modify YEAR/ROUND/SESSION to view different races")
    print("2. Try different lap numbers in visualize_race_snapshot()")
    print("3. Add more analysis: speed maps, pit stops, overtakes")
    print("\nReady for Project 2? 🚀\n")


if __name__ == "__main__":
    main()
