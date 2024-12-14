  def parse_logs(log_file):
    suspicious_keywords = ["failure", "unauthorized", "crashed"]
    alerts = []
    with open(log_file, "r") as f:
        for line in f:
            if any(keyword in line.lower() for keyword in suspicious_keywords):
                alerts.append(line.strip())
    return alerts
