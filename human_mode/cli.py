import sys
from human_mode.reminder import add_reminder, run_reminders, show_report
from human_mode.utils import parse_time


def handle_command():
    args = sys.argv

    if len(args) < 2:
        print("Usage:")
        print(" human add <message> <interval>")
        print(" human run")
        print(" human report")
        return

    command = args[1]

    if command == "add":
        if len(args) < 4:
            print("Usage: human add <message> <interval>")
            return

        message = " ".join(args[2:-1])   # ✅ FIXED
        interval_input = args[-1]
        interval = parse_time(interval_input)

        add_reminder(message, interval)

    elif command == "run":
        run_reminders()

    elif command == "report":
        show_report()

    else:
        print("Unknown command")