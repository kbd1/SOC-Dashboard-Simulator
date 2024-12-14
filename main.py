import os
from log_generator import generate_logs
from log_parser import parse_logs
from visualize import visualize_logs
from elk_config import push_logs_to_elasticsearch

def main():
    log_file = "mock_logs.txt"
    
    # Step 1: Generate Mock Logs
    print("[INFO] Generating mock logs...")
    generate_logs(log_file)
    print(f"[INFO] Logs generated and saved to: {log_file}")

    # Step 2: Parse Logs for Alerts
    print("[INFO] Parsing logs for alerts...")
    alerts = parse_logs(log_file)
    print(f"[INFO] Total alerts found: {len(alerts)}")
    for alert in alerts:
        print(alert)

    # Step 3: Visualize Alerts
    if alerts:
        print("[INFO] Visualizing alerts...")
        visualize_logs(alerts)
    else:
        print("[INFO] No alerts to visualize.")

    # Step 4: Push Logs to ELK Stack
    print("[INFO] Pushing logs to Elasticsearch...")
    try:
        push_logs_to_elasticsearch(log_file)
        print("[INFO] Logs successfully pushed to Elasticsearch.")
    except Exception as e:
        print(f"[ERROR] Failed to push logs to Elasticsearch: {e}")

    # Cleanup (optional)
    print("[INFO] Cleaning up generated log file...")
    if os.path.exists(log_file):
        os.remove(log_file)
        print("[INFO] Log file deleted.")
    else:
        print("[INFO] Log file not found for cleanup.")

if __name__ == "__main__":
    main()
