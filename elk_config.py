from elasticsearch import Elasticsearch

def push_logs_to_elasticsearch(log_file):
    # Elasticsearch configuration
    es = Elasticsearch("http://localhost:9200")
    index_name = "soc-logs"

    with open(log_file, "r") as f:
        for line in f:
            try:
                # Simple log parsing
                timestamp, activity = line.strip().split(" - ")
                doc = {
                    "timestamp": timestamp,
                    "activity": activity
                }
                es.index(index=index_name, document=doc)
            except Exception as e:
                print(f"Error indexing log: {e}")
