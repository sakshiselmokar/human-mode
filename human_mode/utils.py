import psutil
import time

# 🔹 Time parsing (for CLI)
def parse_time(interval_str):
    """
    Converts time like:
    30m -> minutes
    1h -> minutes
    45s -> minutes
    """
    unit = interval_str[-1]
    value = int(interval_str[:-1])

    if unit == "s":
        return value / 60
    elif unit == "m":
        return value
    elif unit == "h":
        return value * 60
    else:
        raise ValueError("Invalid time format. Use s, m, or h.")


# 🔹 Activity detection
def is_user_active(threshold=60):
    """
    Checks CPU usage → basic proxy for activity
    """
    cpu = psutil.cpu_percent(interval=1)
    return cpu > 5  # tweak later


# (Optional for future use)
def is_user_idle(last_activity_time, idle_limit=300):
    return (time.time() - last_activity_time) > idle_limit