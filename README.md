# 🏁 PROJECT 1: THE RACE REPLAY

**F1 Race Visualization using FastF1 API**

A Python project that visualizes Formula 1 races in 2D, showing track layouts and car positions throughout the race.

---

## 📦 Project Structure:

```
Project_1_Race_Replay/
├── README.md                      
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

## 🚀 If you want to try this:

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

### 3️⃣ View the results:
Two images will be created:
- **race_replay_lap_10.png** - Cars at lap 10
- **race_progression.png** - Race evolution at laps 5, 15, 25, 35

---

## 🎯 What you'll learn here:

✅ FastF1 API - Fetching real F1 data  
✅ Data Analysis with Pandas  
✅ Data Visualization with Matplotlib  
✅ Working with telemetry & position data  
✅ Object-Oriented Python  

---

## 📖 Documentation:

### For Setup Help
→ Read **`docs/SETUP_GUIDE.md`**
- Detailed installation steps
- Troubleshooting common issues
- How to modify races/sessions

---

## 🔧 Examples for Customization 

### Change Which Race to Visualize
Edit `project_1_race_replay.py`, find the `main()` function:

```python
def main():
    YEAR = 2024      # Change to 2023, 2022, etc.
    ROUND = 6        # Change to 1-24 (1=Bahrain, 6=Spain, etc.)
    SESSION = 'R'    # Change to 'Q' for qualifying, 'FP1' for practice
```
---

## 📊 Example output

When you run the script, you'll get:

### Terminal output:
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
<img width="1705" height="633" alt="C__WINDOWS_system32_cmd exe - python  project_1_race_replay py 7_6_2026 11_56_56 PM" src="https://github.com/user-attachments/assets/21dd2a78-9648-48d7-917a-7c223d8d30de" />
<img width="1646" height="696" alt="C__WINDOWS_system32_cmd exe - python  project_1_race_replay py 7_6_2026 11_57_02 PM" src="https://github.com/user-attachments/assets/e7771611-82a1-48a7-af5f-f4cb996ec3bf" />

---

### Visual output:
Two PNG files are being shown:
<img width="1600" height="818" alt="Figure 1 7_6_2026 11_55_40 PM" src="https://github.com/user-attachments/assets/de1739b9-db71-467d-9a87-5c4370746165" />
<img width="1594" height="865" alt="Figure 1 7_6_2026 11_56_41 PM" src="https://github.com/user-attachments/assets/e3678721-4dd1-4c45-85a9-668c31e7c4e3" />

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

## 📌 File descriptions:

|          File              |                 Purpose                        |
|----------------------------|------------------------------------------------|
| `project_1_race_replay.py` | Main Python script with all visualization code |
| `requirements.txt`         | List of Python packages needed                 |
| `docs/SETUP_GUIDE.md`      | Detailed installation & setup instructions     |
| `docs/QUICK_REFERENCE.md`  | Code examples, FastF1 basics, debugging        |
| `outputs/`                 | Folder where PNG images are saved              |

---

## 💡 Pro tips:

1. **First run is slow** - Data downloads from internet. Next runs use cache = instant! ⚡
2. **Recent seasons are best** - 2023-2024 have complete data
3. **Experiment fearlessly** - You can't break anything by changing code
4. **Add your own analysis** - Speed profiles, g-force maps, pit stop timing

---

## 🎯 Project goals:

By the end of Project 1, we'll understand:

- [ ] How to use FastF1 to get F1 data
- [ ] Working with pandas DataFrames
- [ ] Creating plots with matplotlib
- [ ] Accessing telemetry & position data
- [ ] Building reusable Python classes
- [ ] Handling real-world data (missing values, edge cases)

---

## ⏭️ What's next?

After mastering Project 1:

- **Project 2: The Pit Wall** 📊 - Real-time dashboard with timing gaps

---
## 👩‍💻 Developed by:

*K. Sailaja*  
B.Tech — Computer Science & Engineering 
