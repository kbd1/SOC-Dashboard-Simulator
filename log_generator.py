from datetime import datetime
import random

def generate_logs(log_file):
    activities = [
        "User login success",
        "User login failure",
        "File accessed",
        "Unauthorized access attempt",
        "Application crashed",
        "Firewall rule triggered"
    ]
    with open(log_file, "w") as f:
        for _ in range(100):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            activity = random.choice(activities)
            f.write(f"{timestamp} - {activity}\n")
