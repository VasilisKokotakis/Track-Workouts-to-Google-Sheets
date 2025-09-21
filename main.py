import os
import requests
from datetime import datetime
import tkinter as tk
from tkinter import messagebox


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


# ---------- Functions ----------
def get_exercises(query: str):
    headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {"query": query, **USER_PROFILE}

    response = requests.post(NUTRITIONIX_ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()
    return response.json().get("exercises", [])


def log_to_sheet(exercise):
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


def on_submit():
    query = entry.get().strip()
    if not query:
        messagebox.showwarning("Input Error", "Please enter an exercise.")
        return

    try:
        exercises = get_exercises(query)
        if not exercises:
            messagebox.showinfo("No Results", "No exercises found for your input.")
            return

        output_box.delete("1.0", tk.END)
        for ex in exercises:
            log_to_sheet(ex)
            msg = f"Logged: {ex['name'].title()} | {ex['duration_min']} min | {ex['nf_calories']} kcal\n"
            output_box.insert(tk.END, msg)

        messagebox.showinfo("Success", "Workout(s) logged successfully!")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("API Error", f"Something went wrong:\n{e}")


# ---------- UI ----------
root = tk.Tk()
root.title("Workout Tracker")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill="both", expand=True)

label = tk.Label(frame, text="Enter activity (e.g., Running 30 min):")
label.pack(anchor="w")

entry = tk.Entry(frame, width=50)
entry.pack(pady=5)

submit_btn = tk.Button(frame, text="Log Workout", command=on_submit)
submit_btn.pack(pady=5)

output_box = tk.Text(frame, height=10, width=60)
output_box.pack(pady=5)

root.mainloop()
