#from parsers.csv_parser import read_csv
#from operator import itemgetter

def normalize_csv_event(event):
    event = {
        "timestamp": "2026-11-07 09:15:22",
        "severity": "INFO",
        "event_type": "USER_LOGIN",
        "username": "jdoe",
        "source_ip": "192.0.2.15"
    }

    timestamp = event.get("timestamp")
    severity = event.get("severity")
    eventtype = event.get("event_type")
    user = event.get("username")
    source = event.get("source_ip")    

    if not timestamp:
        timestamp = None
    if not severity:
        severity = None
    if not eventtype:
        eventtype = None
    if not user:
        user = None
    if not source:
        source = None

    print("Timestamp: " + timestamp + ", Severity: " + severity + ", Event Type: " + eventtype + ", Username: " + user + ", Source IP: " + source)