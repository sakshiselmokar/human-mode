import time
import json
import os
from human_mode.utils import is_user_active
from plyer import notification
FILE = "reminders.json"
STATS_FILE = "stats.json"


# ---------------- REMINDERS ----------------
def load_reminders():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)


def save_reminders(data):
    with open(FILE, "w") as f:
        json.dump(data, f)


def add_reminder(message, interval):
    data = load_reminders()
    data.append({"message": message, "interval": interval})
    save_reminders(data)
    # print(f"Added reminder: {message} every {interval} min")
    if interval < 1:
        print(f"Added reminder: {message} every {int(interval*60)} sec")
    else:
        print(f"Added reminder: {message} every {interval} min")

# ---------------- STATS ----------------
def load_stats():
    if not os.path.exists(STATS_FILE):
        return {"total_reminders": 0, "active_time": 0}
    with open(STATS_FILE, "r") as f:
        return json.load(f)


def save_stats(stats):
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f)


# ---------------- RUN ----------------
def run_reminders():
    reminders = load_reminders()

    if not reminders:
        print("No reminders found")
        return

    print("Running smart reminders... (Ctrl+C to stop)")

    current_time = time.time()
    last_trigger = [current_time] * len(reminders)
    focus_start = current_time

    stats = load_stats()

    while True:
        current_time = time.time()
        active = is_user_active()

        for i, r in enumerate(reminders):

            next_time = last_trigger[i] + (r["interval"] * 60)

            if current_time >= next_time:
                if active:
                    print(f"\n💡 You've been working continuously. {r['message']}?")
                    
                    notification.notify(
                        title="🧠 Human Mode",
                        message=r['message'],
                        timeout=5
                    )

                    stats["total_reminders"] += 1
                
                else:
                    # print(f"\n😴 Skipping (idle): {r['message']}")
                    last_trigger[i] = current_time
                    continue

                last_trigger[i] = current_time

        # track active time
        if active:
            stats["active_time"] += 5  # loop runs every 5 sec

        save_stats(stats)

        # burnout detection
        if active and (current_time - focus_start > 7200):
            print("\n⚠️ You've been working for 2+ hours. Take a break!")

            notification.notify(
                title="⚠️ Burnout Alert",
                message="You've been working for 2+ hours. Take a break!",
                timeout=5
            )            
            focus_start = current_time

        time.sleep(5)


# ---------------- REPORT ----------------
def show_report():
    stats = load_stats()

    total = stats["total_reminders"]
    active_time = stats["active_time"] / 60  # seconds → minutes

    if active_time > 120:
        burnout = "High ⚠️"
    elif active_time > 60:
        burnout = "Moderate 😐"
    else:
        burnout = "Low 😊"

    print("\n📊 Human Mode Report")
    print(f"Total reminders: {total}")
    print(f"Active time: {round(active_time, 2)} minutes")
    print(f"Burnout risk: {burnout}")
    