# PROJECT 1: THE RACE REPLAY 🏁
## F1 Race Visualization Setup Guide

---

## 📋 What You'll Learn

✅ How to use the **FastF1 API** to fetch F1 data  
✅ Working with **Pandas** for data manipulation  
✅ Creating 2D track visualizations with **Matplotlib**  
✅ Handling F1-specific data (positions, telemetry, drivers)  
✅ Building a reusable class-based structure  

---

## 🛠️ Installation

### Step 1: Install Python (if not already installed)
Ensure you have **Python 3.10+**

Check version:
```bash
python --version
```

### Step 2: Create a Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Packages

Create a file named `requirements.txt` with this content:
```
fastf1==0.4.8
matplotlib==3.8.2
pandas==2.1.3
numpy==1.26.2
```

Then install:
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install fastf1 matplotlib pandas numpy
```

---

## 🚀 Running the Project

### Quick Start
```bash
python project_1_race_replay.py
```

This will:
1. Load the **2024 Spanish GP** race data
2. Display race statistics (top 10 finishers)
3. Create visualizations of car positions at different laps
4. Save PNG files of the visualizations

### Modify to View Different Races

Edit the `main()` function in the script:

```python
def main():
    YEAR = 2024      # Change to any year 2018+
    ROUND = 6        # Change to round number (1-24)
    SESSION = 'R'    # 'R'=Race, 'Q'=Qualifying, 'FP1'=Practice1, etc.
```

**Example: 2023 Monaco Grand Prix (Qualifying)**
```python
YEAR = 2023
ROUND = 5
SESSION = 'Q'
```

---

## 📊 Understanding the Code

### Main Class: `F1RaceReplay`

**Initialization:**
```python
replay = F1RaceReplay(year=2024, round_num=6, session_name='R')
```

**Key Methods:**

| Method | Purpose |
|--------|---------|
| `load_session()` | Fetches data from FastF1 API |
| `plot_track()` | Draws the track layout |
| `visualize_race_snapshot(lap_num)` | Shows car positions at a specific lap |
| `visualize_positions_multiple_laps()` | Grid view of race progression |
| `get_lap_stats()` | Displays race statistics |

**Example: View a specific lap**
```python
replay = F1RaceReplay(2024, 6, 'R')
replay.load_session()
fig = replay.visualize_race_snapshot(lap_num=15)
plt.show()
```

---

## 🎨 Customization Ideas

### Add Pit Stop Visualization
```python
def show_pit_stops(self, ax):
    pit_stop_laps = self.session.laps[self.session.laps['PitOutTime'].notna()]
    for lap in pit_stop_laps.iterrows():
        # Mark pit stops on track
```

### Show Speed Heatmap
```python
def plot_speed_heatmap(self):
    fastest_lap = self.session.laps.pick_fastest()
    telemetry = fastest_lap.telemetry
    # Use telemetry['Speed'] to color track segments
```

### Track Overtakes
```python
def detect_overtakes(self):
    # Compare driver positions lap to lap
    # Find when position changes
```

---

## 📌 Common Issues & Solutions

### Issue: "No module named 'fastf1'"
**Solution:** Reinstall FastF1
```bash
pip install --upgrade fastf1
```

### Issue: "No data available for session"
**Solution:** 
- Check the YEAR/ROUND/SESSION values are correct
- Some historic sessions may not have full data
- Try a recent season (2022-2024)

### Issue: "Connection timeout"
**Solution:** 
- FastF1 uses internet to fetch data
- Check your connection
- Data is cached after first load, so next run will be faster

### Issue: "Empty plot"
**Solution:** 
- Some laps may have incomplete telemetry data
- Try different lap numbers
- Check `replay.session.laps` to see available data

---

## 🔗 FastF1 API Resources

Key objects you'll use:
- `session.laps` - DataFrame of all laps with timing data
- `lap.telemetry` - Detailed point-by-point position/speed data
- `session.results` - Final race results and standings
- `session.event` - Race info (name, location, date)

FastF1 Docs: https://theoehrly.github.io/FastF1/

---

## 📈 What's Next?

Once you master Project 1:
- **Project 2:** Build a real-time pit wall dashboard (timing deltas)
- **Project 3:** Create the full-stack web app (FastF1 + Flask + React)

---

## 💡 Pro Tips

1. **Cache data locally** - First run takes longer, subsequent runs are instant
2. **Recent races have better data** - 2023-2024 seasons are most complete
3. **Experiment with different visualizations** - Add speed maps, g-force data, etc.
4. **Save high-DPI images** - Use `dpi=300` for printing

---

Happy coding! 🏎️ Feel free to reach out if you hit any issues!
