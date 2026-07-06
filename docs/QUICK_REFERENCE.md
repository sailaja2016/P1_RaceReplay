# PROJECT 1: QUICK REFERENCE GUIDE 📚

## Key Concepts Explained

---

## 1️⃣ FASTF1 API BASICS

### What is FastF1?
FastF1 is a Python library that **fetches official F1 data** and processes it for analysis. It uses F1TV/FIA data.

### Loading a Session
```python
import fastf1

# Enable caching (speeds up repeated downloads)
fastf1.Cache.enable_cache('/tmp/fastf1_cache')

# Get a specific session
session = fastf1.get_session(year=2024, round=6, session='R')
session.load()  # This fetches the data from the internet
```

**Session Types:**
- `'FP1'` - Free Practice 1
- `'FP2'` - Free Practice 2  
- `'FP3'` - Free Practice 3
- `'Q'` - Qualifying
- `'R'` - Race

### Accessing Session Data
```python
# All laps (DataFrame)
laps = session.laps

# Race results
results = session.results

# Event information
print(session.event['EventName'])      # "Spanish Grand Prix"
print(session.event['Location'])       # "Barcelona"
print(session.event['Date'])           # Race date

# Fastest lap of session
fastest_lap = session.laps.pick_fastest()
```

---

## 2️⃣ WORKING WITH LAPS & TELEMETRY

### Understanding Laps DataFrame
```python
# Each row is ONE lap by ONE driver
laps_df = session.laps

# Important columns:
# - 'Driver': Driver abbreviation (e.g., 'VER', 'HAM')
# - 'DriverNumber': Car number (1-99)
# - 'LapNumber': Which lap of the race (1, 2, 3...)
# - 'LapTime': How long the lap took (timedelta)
# - 'Position': Current position in race
# - 'Sector1Time', 'Sector2Time', 'Sector3Time': Sector times

# Filter laps by driver
ver_laps = laps_df[laps_df['Driver'] == 'VER']

# Filter laps by lap number
lap_10 = laps_df[laps_df['LapNumber'] == 10]

# Get fastest lap by a driver
ver_fastest = ver_laps.pick_fastest()
```

### Accessing Telemetry Data
Each lap has detailed **telemetry** = position/speed data recorded many times per second

```python
lap = session.laps.iloc[0]  # Get first lap
telemetry = lap.telemetry

# Each telemetry point has:
# - 'X': X position on track (meters)
# - 'Y': Y position on track (meters)
# - 'Z': Elevation
# - 'Speed': Car speed (km/h)
# - 'Throttle': Throttle percentage (0-100)
# - 'Brake': Brake percentage (0-100)
# - 'Gear': Current gear (1-8)

# Access as pandas Series
x_positions = telemetry['X'].values   # numpy array
y_positions = telemetry['Y'].values
speeds = telemetry['Speed'].values
```

**Example: Get final position of car in lap**
```python
lap = session.laps.iloc[0]
telemetry = lap.telemetry

final_x = telemetry['X'].iloc[-1]  # Last X position
final_y = telemetry['Y'].iloc[-1]  # Last Y position
final_speed = telemetry['Speed'].iloc[-1]  # Final speed
```

---

## 3️⃣ PLOTTING WITH MATPLOTLIB

### Basic Plot Structure
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 8))

# Draw something
ax.plot([0, 1], [0, 1])  # Line from (0,0) to (1,1)
ax.scatter([0.5], [0.5])  # Point at (0.5, 0.5)

# Customize
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('My Plot')
ax.grid(True)
ax.legend()

# Show or save
plt.show()
plt.savefig('output.png', dpi=150)
```

### Drawing the F1 Track
```python
# Track is a series of X,Y coordinates
track_coords = np.column_stack([x_positions, y_positions])

# Draw track as a line
ax.plot(track_coords[:, 0], track_coords[:, 1], 'k-', linewidth=2)

# Fill inside of track
ax.fill(track_coords[:, 0], track_coords[:, 1], color='green', alpha=0.1)

# Mark start/finish
ax.plot(track_coords[0, 0], track_coords[0, 1], 'r*', markersize=20)
```

### Plotting Cars (Scatter Points)
```python
# Plot a car at position (x, y)
ax.scatter(x, y, s=300, c='red', edgecolors='black', linewidth=2)

# Add label
ax.text(x, y-100, 'VER', ha='center', fontsize=10, fontweight='bold')
```

### Using Colors
```python
# Define color palette
colors = {
    'RED': '#DC0000',      # Ferrari
    'BLUE': '#0082FA',     # Alpine
    'ORANGE': '#FF8700',   # McLaren
    'CYAN': '#00D2BE',     # Aston Martin
}

# Use it
ax.scatter(x, y, c=colors['RED'])
```

---

## 4️⃣ DATA MANIPULATION WITH PANDAS

### Filtering DataFrames
```python
import pandas as pd

# Filter by condition
young_drivers = laps_df[laps_df['DriverNumber'] < 10]

# Multiple conditions (& = AND, | = OR)
mercedes_at_lap_5 = laps_df[(laps_df['Team'] == 'Mercedes') & (laps_df['LapNumber'] == 5)]

# Get specific rows/columns
first_lap = laps_df[laps_df['LapNumber'] == 1]
driver_names = laps_df['Driver'].unique()
```

### Iterating Through Data
```python
# Loop through each row
for idx, row in laps_df.iterrows():
    driver = row['Driver']
    lap_time = row['LapTime']
    print(f"{driver}: {lap_time}")

# Better: loop with iterrows() preserves index
for _, lap in laps_df.iterrows():
    position = lap['Position']
    telemetry = lap.telemetry
    # Do something with each lap
```

### Sorting & Ranking
```python
# Sort by LapTime (fastest first)
fastest_laps = laps_df.sort_values('LapTime')

# Get top 5 drivers
top_5 = laps_df.nlargest(5, 'Position')

# Get unique drivers
unique_drivers = laps_df['Driver'].unique()
```

---

## 5️⃣ PUTTING IT TOGETHER: REAL EXAMPLES

### Example 1: Plot One Lap
```python
import fastf1
import matplotlib.pyplot as plt

session = fastf1.get_session(2024, 6, 'R')
session.load()

# Get specific lap
laps_lap_10 = session.laps[session.laps['LapNumber'] == 10]

fig, ax = plt.subplots(figsize=(14, 10))

# Plot each car at lap 10
for _, lap in laps_lap_10.iterrows():
    if lap.telemetry is not None:
        x = lap.telemetry['X'].iloc[-1]
        y = lap.telemetry['Y'].iloc[-1]
        
        ax.scatter(x, y, s=300, c='blue', edgecolors='black')
        ax.text(x, y, lap['Driver'], ha='center')

ax.set_aspect('equal')
ax.set_title('Car Positions at Lap 10')
plt.show()
```

### Example 2: Speed Profile of Fastest Lap
```python
fastest_lap = session.laps.pick_fastest()
telemetry = fastest_lap.telemetry

# Get distance along track and speed
distance = telemetry['Distance'].values
speed = telemetry['Speed'].values

fig, ax = plt.subplots()
ax.plot(distance, speed, linewidth=2)
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Speed (km/h)')
ax.set_title(f'Fastest Lap Speed Profile: {fastest_lap["Driver"]}')
ax.grid(True)
plt.show()
```

### Example 3: Track Evolution (Speed at Different Laps)
```python
fig, ax = plt.subplots()

for lap_num in [5, 10, 20, 30]:
    laps = session.laps[session.laps['LapNumber'] == lap_num]
    
    for _, lap in laps.iterrows():
        if lap.telemetry is not None:
            distance = lap.telemetry['Distance'].values
            speed = lap.telemetry['Speed'].values
            ax.plot(distance, speed, label=f'Lap {lap_num}', alpha=0.7)

ax.set_xlabel('Distance (m)')
ax.set_ylabel('Speed (km/h)')
ax.set_title('Track Evolution - Speed Profile')
ax.legend()
ax.grid(True)
plt.show()
```

---

## 6️⃣ DEBUGGING TIPS

### Check what data you have
```python
# See all columns in laps
print(laps_df.columns)

# See shape (rows, columns)
print(laps_df.shape)

# Look at first few rows
print(laps_df.head())

# Check if telemetry exists
lap = laps_df.iloc[0]
if lap.telemetry is None:
    print("No telemetry data for this lap!")
else:
    print(f"Telemetry points: {len(lap.telemetry)}")
```

### Handle Missing Data
```python
# Skip laps without telemetry
for _, lap in laps_df.iterrows():
    if lap.telemetry is not None:  # Check first!
        telemetry = lap.telemetry
        # Now safe to use telemetry
```

### Print debug info
```python
print(f"Session: {session.event['EventName']}")
print(f"Total laps: {session.laps.shape[0]}")
print(f"Unique drivers: {len(session.laps['Driver'].unique())}")
print(f"Max laps completed: {session.laps['LapNumber'].max()}")
```

---

## 7️⃣ NEXT LEVEL FEATURES

Once you understand the basics, try these:

### 1. Pit Stop Visualization
```python
pit_stops = session.laps[session.laps['PitOutTime'].notna()]
# Mark where pit stops happened
```

### 2. Gap Analysis
```python
# Compare lap times
leader = session.laps.pick_driver('VER')
challenger = session.laps.pick_driver('LEC')
gap = leader['LapTime'] - challenger['LapTime']
```

### 3. Position Changes
```python
# Find overtakes
for i in range(len(laps)-1):
    current_pos = laps.iloc[i]['Position']
    next_pos = laps.iloc[i+1]['Position']
    if current_pos > next_pos:
        print(f"Overtake! {laps.iloc[i]['Driver']}")
```

### 4. Create Animation
```python
from matplotlib.animation import FuncAnimation

def update(frame):
    # Clear and redraw for each frame
    ax.clear()
    # Plot lap frame
    
ani = FuncAnimation(fig, update, frames=100, interval=50)
ani.save('animation.gif')
```

---

## 📖 Useful Resources

- **FastF1 Documentation**: https://theoehrly.github.io/FastF1/
- **Pandas Cheat Sheet**: https://pandas.pydata.org/docs/
- **Matplotlib Gallery**: https://matplotlib.org/stable/gallery/
- **F1 Data Analysis Blog**: https://www.theoehrly.com/

---

## 🎯 Learning Checklist

As you work through Project 1, check off these skills:

- [ ] Load F1 session data with FastF1
- [ ] Access lap and telemetry data
- [ ] Filter DataFrames with pandas
- [ ] Create plots with matplotlib
- [ ] Handle missing data gracefully
- [ ] Plot the track layout
- [ ] Show car positions on track
- [ ] Create multi-subplot visualizations
- [ ] Understand coordinate systems (X, Y on track)
- [ ] Use team colors effectively

Once all checked, you're ready for **Project 2**! 🚀

---

Good luck! 🏎️
