from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

PASSWORD = os.getenv("APP_PASSWORD")

@app.route("/")
def home():
    return "Vulnerable App"

@app.route("/ping")
def ping():
    host = request.args.get("host")
    result = subprocess.check_output(["ping", "-c", "1", host])
    return result

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
