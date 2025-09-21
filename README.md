--

````markdown
# Track Workouts to Google Sheets

A simple Python script that logs your workouts to **Google Sheets**.  
It uses the [Nutritionix API](https://developer.nutritionix.com/) to parse natural-language exercise descriptions and the [Sheety API](https://sheety.co/) to record the results in a spreadsheet.

--

## ✨ Features
- Accepts free-text exercise input (e.g., *"Running 30 minutes"*, *"Cycling 45 min"*).
- Fetches duration and calories burned from Nutritionix.
- Logs date, time, exercise, duration, and calories into Google Sheets.
- Uses environment variables to keep sensitive credentials safe.
- Handles API errors gracefully.

---

## ⚙️ Requirements
- Python 3.8+
- `requests` library

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

Run the script:

```bash
python exercise_logger.py
```

Example interaction:

```
Activity & duration (e.g., Cycling – 45 min): Running 30 minutes
✅ Logged: Running | 30 min | 350 kcal
```

Check your Google Sheet — the data should appear automatically.

---

## 📂 Project Structure

```
.
├── exercise_logger.py   # Main script
└── README.md            # Documentation
```

---

## 🚀 Future Improvements

* Support multiple activities in one input (comma-separated).
* Add daily/weekly summary reports.
* Dockerize for easy deployment.

---

## 📝 License

This project is licensed under the MIT License.


