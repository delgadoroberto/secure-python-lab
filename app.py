from flask import Flask, request
import subprocess

app = Flask(__name__)

PASSWORD = "SuperSecret123"

@app.route("/")
def home():
    return "Vulnerable App"

@app.route("/ping")
def ping():
    host = request.args.get("host")
    result = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return result

@app.route("/eval")
def dangerous():
    data = request.args.get("data")
    return str(eval(data))

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
