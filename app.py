from flask import Flask, request
import subprocess
import os
import re

app = Flask(__name__)

PASSWORD = os.getenv("APP_PASSWORD")


@app.route("/")
def home():
    return "Secure App"


@app.route("/ping")
def ping():
    host = request.args.get("host")

    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return "Invalid host", 400

    result = subprocess.check_output(
        ["/bin/ping", "-c", "1", host]
    )

    return result


@app.route("/secret")
def secret():

    provided_password = request.headers.get("X-Password")

    if not PASSWORD:
        return "Server misconfiguration", 500

    if provided_password != PASSWORD:
        return "Unauthorized", 401

    return {
        "message": "Access granted",
        "status": "success"
    }


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
