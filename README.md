Here’s a more complete README.md file and the updated code integrating the ELK stack as a module for real-time log processing.

README.md

# SOC Dashboard Simulator

A Python-based tool that simulates Security Operations Center (SOC) functionalities, focusing on log monitoring, alerting, and visualizing suspicious activities.

This project is designed for cybersecurity students and professionals looking to gain hands-on experience with basic SOC workflows and tools like the ELK stack.

---

## Features

1. **Log Monitoring**:
   - Parses system logs for suspicious activities such as unauthorized access attempts, login failures, or application crashes.
   - Detects keywords in logs to trigger alerts.

2. **Alerting**:
   - Highlights suspicious activities and categorizes alerts into Failures, Unauthorized Access Attempts, and Crashes.

3. **Visualization**:
   - Displays a breakdown of alerts using bar graphs with `matplotlib`.

4. **Real-time Log Processing**:
   - Integration with the ELK stack for real-time log ingestion, parsing, and dashboard visualization.

---

## Prerequisites

1. **Python Packages**:
   Install required Python libraries:
   ```bash
   pip install matplotlib elasticsearch

	2.	ELK Stack:
Set up the ELK stack (Elasticsearch, Logstash, Kibana). Ensure it is running locally or on a server:
	•	Elasticsearch: http://localhost:9200
	•	Logstash: Use the provided configuration file.
	•	Kibana: Access through http://localhost:5601.

## Installation
	1.	Clone this repository:

git clone https://github.com/your_username/soc-dashboard-simulator.git
cd soc-dashboard-simulator


	2.	Configure the ELK Module:
	•	Edit elk_config.py with your Elasticsearch endpoint and index details.
	3.	Run the program:

python main.py

## File Structure

.
├── main.py            # Main program
├── log_generator.py   # Mock log generator
├── log_parser.py      # Log parsing for alerts
├── visualize.py       # Alert visualization
├── elk_config.py      # ELK Stack integration
├── mock_logs.txt      # Example log file (generated)
├── README.md          # Project documentation

## ELK Integration

This tool uses an Elasticsearch client to push logs in real time. Logs are stored and visualized using Kibana dashboards.
	1.	Logstash Configuration:
Use the following Logstash configuration (logstash.conf):

input {
    file {
        path => "/path/to/mock_logs.txt"
        start_position => "beginning"
    }
}
filter {
    grok {
        match => { "message" => "%{TIMESTAMP_ISO8601:timestamp} - %{GREEDYDATA:activity}" }
    }
}
output {
    elasticsearch {
        hosts => ["http://localhost:9200"]
        index => "soc-logs"
    }
    stdout {}
}


	2.	Kibana Dashboard:
	•	Access http://localhost:5601 and import logs from the soc-logs index.
	•	Create visualizations for suspicious activities.

## Future Enhancements
	•	Role-based access control for SOC analysts.
	•	Integration with third-party APIs for alerting (e.g., Slack, email).
	•	Machine learning module for anomaly detection.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

