import matplotlib.pyplot as plt

def visualize_logs(alerts):
    categories = ["Failures", "Unauthorized", "Crashes"]
    counts = [
        sum(1 for alert in alerts if "failure" in alert.lower()),
        sum(1 for alert in alerts if "unauthorized" in alert.lower()),
        sum(1 for alert in alerts if "crashed" in alert.lower())
    ]

    plt.bar(categories, counts, color=["red", "orange", "blue"])
    plt.title("SOC Alerts Breakdown")
    plt.ylabel("Number of Alerts")
    plt.xlabel("Alert Categories")
    plt.show()
