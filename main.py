import os
import requests
from datetime import datetime
import sys


# ---------- Configuration ----------
NUTRITIONIX_APP_ID = os.getenv("NT_APP_ID")
NUTRITIONIX_API_KEY = os.getenv("NT_API_KEY")
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

USER_PROFILE = {
    "gender": "Male",
    "weight_kg": 80,
    "height_cm": 190,
    "age": 30
}

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"


# ---------- Helpers ----------
def check_env_vars():
    """Ensure all required environment variables exist."""
    missing = [
        var for var, value in {
            "NT_APP_ID": NUTRITIONIX_APP_ID,
            "NT_API_KEY": NUTRITIONIX_API_KEY,
            "SHEET_ENDPOINT": SHEET_ENDPOINT,
            "BEARER_TOKEN": BEARER_TOKEN,
        }.items() if not value
    ]
    if missing:
        sys.exit(f"❌ Missing environment variables: {', '.join(missing)}")


def get_exercises(query: str):
    """Send query to Nutritionix API and return parsed response."""
    headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "query": query,
        **USER_PROFILE
    }

    response = requests.post(NUTRITIONIX_ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()
    return response.json().get("exercises", [])


def log_to_sheet(exercise):
    """Send exercise data to Google Sheet via Sheety API."""
    now = datetime.now()
    data = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    headers = {"Authorization": BEARER_TOKEN}
    response = requests.post(SHEET_ENDPOINT, json=data, headers=headers)
    response.raise_for_status()
    return response.json()


# ---------- Main ----------
def main():
    check_env_vars()

    query = input("Activity & duration (e.g., Cycling – 45 min): ")
    try:
        exercises = get_exercises(query)
        if not exercises:
            print("⚠️ No exercises found for your input.")
            return

        for exercise in exercises:
            sheet_response = log_to_sheet(exercise)
            print(f"✅ Logged: {exercise['name'].title()} | "
                  f"{exercise['duration_min']} min | "
                  f"{exercise['nf_calories']} kcal")
            print("Sheety response:", sheet_response)

    except requests.exceptions.RequestException as e:
        print("❌ API request failed:", e)


if __name__ == "__main__":
    main()
