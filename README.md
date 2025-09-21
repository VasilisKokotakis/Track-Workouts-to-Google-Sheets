
# Track Workouts to Google Sheets

A simple Python app with a **basic GUI** that logs your workouts to **Google Sheets**.  
It uses the [Nutritionix API](https://developer.nutritionix.com/) to parse natural-language exercise descriptions and the [Sheety API](https://sheety.co/) to record the results in a spreadsheet.

---

## ✨ Features
- Enter exercises in natural language (e.g., *"Running 30 minutes"*, *"Cycling 45 min"*).
- Fetches duration and calories burned from Nutritionix.
- Logs date, time, exercise, duration, and calories into Google Sheets.
- Provides a basic graphical interface (Tkinter).
- Uses environment variables to keep sensitive credentials safe.
- Error handling for API requests.

---

## ⚙️ Requirements
- Python 3.8+
- `requests` library
- `tkinter` (comes pre-installed with most Python distributions)

Install dependencies:
```bash
pip install requests
````

---

## 🔑 Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/VasilisKokotakis/track-workouts-to-google-sheets.git
   cd track-workouts-to-google-sheets
   ```

2. **Set up environment variables**

   You need credentials from Nutritionix and Sheety.
   Export them in your shell (or add to `.bashrc` / `.zshrc`):

   ```bash
   export NT_APP_ID="your_nutritionix_app_id"
   export NT_API_KEY="your_nutritionix_api_key"
   export SHEET_ENDPOINT="your_sheety_endpoint"
   export BEARER_TOKEN="Bearer your_sheety_token"
   ```

3. **Create a Google Sheet**

   * Connect it to Sheety.
   * Ensure the sheet has columns for:
     `date | time | exercise | duration | calories`.

---

## ▶️ Usage

Run the app:

```bash
python exercise_logger.py
```

You’ll see a small window where you can:

1. Enter an activity (e.g., *"Running 30 minutes"*).
2. Click **Log Workout**.
3. View results in the output box.

Example:

```
Logged: Running | 30 min | 350 kcal
```

Your workout will also be added to your Google Sheet automatically.

---

## 📂 Project Structure

```
.
├── main.py              # Main app with GUI
└── README.md            # Documentation
```

---

## 🚀 Future Improvements

* Support multiple activities in one input (comma-separated).
* Add daily/weekly summary reports.
* Improve UI with modern styling (e.g., custom widgets, themes).
* Package as an executable for non-Python users.

---

## 📝 License

This project is licensed under the MIT License.

