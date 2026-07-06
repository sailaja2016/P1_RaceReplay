# 🏁 PROJECT 1: THE RACE REPLAY

**F1 Race Visualization using FastF1 API**

A Python project that visualizes Formula 1 races in 2D, showing track layouts and car positions throughout the race.

---

## 📦 Project Structure

```
Project_1_Race_Replay/
├── README.md                      ← You are here
├── requirements.txt               ← All Python packages to install
├── project_1_race_replay.py      ← Main Python script
├── docs/
│   ├── SETUP_GUIDE.md            ← Detailed installation & setup
│   └── QUICK_REFERENCE.md        ← Code examples & explanations
└── outputs/                       ← Where visualizations save
    ├── race_replay_lap_10.png    (generated when you run)
    └── race_progression.png      (generated when you run)
```

---

## 🚀 QUICK START (5 Minutes)

### 1️⃣ Install Python Packages
Open your terminal/command prompt and run:

```bash
pip install -r requirements.txt
```

**What it does:** Installs FastF1, Matplotlib, Pandas, NumPy

### 2️⃣ Run the Project
```bash
python project_1_race_replay.py
```

**What happens:**
- Downloads 2024 Spanish Grand Prix data (happens once, then cached)
- Displays race statistics in terminal
- Creates 2 PNG visualizations in the `outputs/` folder
- Opens visualization windows

### 3️⃣ View the Results
Two images will be created:
- **race_replay_lap_10.png** - Cars at lap 10
- **race_progression.png** - Race evolution at laps 5, 15, 25, 35

---

## 🎯 What You'll Learn

✅ FastF1 API - Fetching real F1 data  
✅ Data Analysis with Pandas  
✅ Data Visualization with Matplotlib  
✅ Working with telemetry & position data  
✅ Object-Oriented Python  

---

## 📖 Documentation

### For Setup Help
→ Read **`docs/SETUP_GUIDE.md`**
- Detailed installation steps
- Troubleshooting common issues
- How to modify races/sessions

### For Code Learning
→ Read **`docs/QUICK_REFERENCE.md`**
- FastF1 API explained
- Code examples
- Debugging tips
- How to customize visualizations

---

## 🔧 Customization Examples

### Change Which Race to Visualize
Edit `project_1_race_replay.py`, find the `main()` function:

```python
def main():
    YEAR = 2024      # Change to 2023, 2022, etc.
    ROUND = 6        # Change to 1-24 (1=Bahrain, 6=Spain, etc.)
    SESSION = 'R'    # Change to 'Q' for qualifying, 'FP1' for practice
```

**Examples:**
- 2024 Monaco GP: `YEAR=2024, ROUND=5`
- 2023 Silverstone (British GP): `YEAR=2023, ROUND=10`
- 2024 Abu Dhabi GP (Qualifying): `YEAR=2024, ROUND=24, SESSION='Q'`

### Change Which Laps to Visualize
In `main()`, modify these lines:

```python
# Single lap
fig1 = replay.visualize_race_snapshot(lap_num=20)  # Change 20 to any lap

# Multiple laps
fig2 = replay.visualize_positions_multiple_laps(lap_numbers=[10, 20, 30, 40])
```

---

## 📊 Example Output

When you run the script, you'll get:

### Terminal Output:
```
============================================================
PROJECT 1: F1 RACE REPLAY 🏁
============================================================

Loading 2024 Round 6 (R)...
✓ Session loaded: Spanish Grand Prix
  Circuit: Barcelona

============================================================
RACE STATISTICS: Spanish Grand Prix
============================================================

Top 10 Finishers:
 1. VER - Team: Red Bull Racing            - Points: 25
 2. LEC - Team: Scuderia Ferrari           - Points: 18
 3. SAI - Team: Scuderia Ferrari           - Points: 15
...
```

### Visual Output:
Two PNG files showing:
- Track layout with grid lines
- Car positions as colored circles
- Driver names and numbers
- Start/finish line marked

---

## ❓ Troubleshooting

### Problem: "No module named 'fastf1'"
```bash
pip install --upgrade fastf1
```

### Problem: "Connection timeout" or "No data"
- Check internet connection
- Try a recent season (2023-2024 has best data)
- Wait a few seconds and try again

### Problem: "Empty or incomplete plots"
- Some older seasons have incomplete data
- Try a different race/session
- Check `docs/SETUP_GUIDE.md` for full troubleshooting

---

## 📚 Key Concepts

### Session Types
- `'FP1'` = Free Practice 1
- `'FP2'` = Free Practice 2
- `'FP3'` = Free Practice 3
- `'Q'` = Qualifying
- `'R'` = Race

### What's Being Visualized
- **Track Layout** - Outline of the circuit
- **Car Positions** - Where each car is at a specific lap
- **Team Colors** - Ferrari red, Mercedes silver, etc.
- **Driver Info** - Three-letter abbreviation + car number

---

## 🎓 Next Steps

1. **Run the script as-is** - Get familiar with the output
2. **Try different races** - Experiment with different YEAR/ROUND values
3. **Customize visualizations** - Change lap numbers, add new features
4. **Read the docs** - Deep dive into FastF1 API and Pandas
5. **Add features** - Speed maps, pit stop analysis, overtake detection

---

## 📌 File Descriptions

| File | Purpose |
|------|---------|
| `project_1_race_replay.py` | Main Python script with all visualization code |
| `requirements.txt` | List of Python packages needed |
| `docs/SETUP_GUIDE.md` | Detailed installation & setup instructions |
| `docs/QUICK_REFERENCE.md` | Code examples, FastF1 basics, debugging |
| `outputs/` | Folder where PNG images are saved |

---

## 💡 Pro Tips

1. **First run is slow** - Data downloads from internet. Next runs use cache = instant! ⚡
2. **Recent seasons are best** - 2023-2024 have complete data
3. **Experiment fearlessly** - You can't break anything by changing code
4. **Add your own analysis** - Speed profiles, g-force maps, pit stop timing

---

## 🚀 Ready to Start?

```bash
# 1. Install packages
pip install -r requirements.txt

# 2. Run the project
python project_1_race_replay.py

# 3. Check outputs/ folder for PNG images
```

---

## 📞 Help & Support

- **Setup issues?** → Check `docs/SETUP_GUIDE.md`
- **Don't understand code?** → Check `docs/QUICK_REFERENCE.md`
- **Want to customize?** → Read the Python comments in `project_1_race_replay.py`

---

## 🎯 Project Goals

By the end of Project 1, you'll understand:

- [ ] How to use FastF1 to get F1 data
- [ ] Working with pandas DataFrames
- [ ] Creating plots with matplotlib
- [ ] Accessing telemetry & position data
- [ ] Building reusable Python classes
- [ ] Handling real-world data (missing values, edge cases)

---

## ⏭️ What's Next?

After mastering Project 1:

- **Project 2: The Pit Wall** 📊 - Real-time dashboard with timing gaps
- **Project 3: The Web Paddock** 🌐 - Full-stack web app (React + FastAPI)

---

**Happy coding! Let's go racing! 🏎️💨**
