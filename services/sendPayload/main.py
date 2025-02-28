import requests
import json

def send(payload, logstashEndpoint, logstashPort):
    print(f"Sending payload: {json.dumps(payload, indent=2)}")
    headers = {
        'Content-Type': 'application/json'
    }
    logstash = f"http://{logstashEndpoint}:{logstashPort}"
    print(f"Sending to {logstash}")
    try:
        response = requests.post(logstash, data=json.dumps(payload), headers=headers)
        return response.status_code
    except Exception as payloadSendError:
        errorInSend = f"Error occured in sending to {logstash}, ERROR: {payloadSendError}"
        print(errorInSend)
        return errorInSend