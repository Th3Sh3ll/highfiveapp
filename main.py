from flask import Flask, render_template, request
from services.sendPayload.main import send

app = Flask(__name__)

print(f"Loading variables")
logstashEndpoint = ''
logstashPort     = 5099


@app.route('/payload', methods=['POST'])
def sendToLogstash():
    payload = request.get_json()
    responseFromLogstash = send(payload, logstashEndpoint, logstashPort)
    return render_template (
        'homePage.html',
        responseCode = responseFromLogstash
    )


@app.route('/')
def homePage():
    return render_template(
        'homePage.html'
    )


if __name__ == '__main__':
    app.debug = True
    app.run()