# 🔐 Secure Python Lab

## Overview

Secure Python Lab is a hands-on project designed to demonstrate secure Python application development practices and automated security testing within a CI/CD pipeline.

The repository contains a simple Flask application, a Docker container definition, and a GitHub Actions workflow that performs static code analysis, secret detection, and vulnerability scanning.

This lab is intended for cybersecurity professionals, DevSecOps engineers, and developers interested in integrating security controls into software development workflows.

---

## Objectives

This project demonstrates how to:

- Develop a simple Python web application
- Implement basic input validation
- Containerize applications with Docker
- Integrate automated security checks into GitHub Actions
- Detect insecure coding patterns
- Identify exposed secrets
- Scan dependencies and filesystems for vulnerabilities

---

## Repository Structure

```text
secure-python-lab/
├── .github/
│   └── workflows/
│       └── security.yml
├── Dockerfile
├── app.py
├── requirements.txt
└── README.md
```

---

## Application Description

The application exposes two endpoints.

### `/`

Returns a simple message indicating that the application is running.

Example:

```bash
curl http://localhost:5000/
```

Output:

```text
Secure App
```

---

### `/ping`

Accepts a hostname parameter and performs a system ping.

Example:

```bash
curl "http://localhost:5000/ping?host=google.com"
```

The application validates the input using a regular expression before executing the command.

Validation pattern:

```python
^[a-zA-Z0-9.-]+$
```

The ping command is executed safely using:

```python
subprocess.check_output(
    ["/bin/ping", "-c", "1", host]
)
```

This avoids command injection vulnerabilities associated with `shell=True`.

---

## Running Locally

### Clone the repository

```bash
git clone https://github.com/<your-username>/secure-python-lab.git

cd secure-python-lab
```

### Create a virtual environment

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

```bash
export APP_PASSWORD="StrongPassword123!"
```

### Run the application

```bash
python app.py
```

---

## Running with Docker

Build the image:

```bash
docker build -t secure-python-lab .
```

Run the container:

```bash
docker run -p 5000:5000 secure-python-lab
```

---

## Security Pipeline

The GitHub Actions workflow automatically executes security checks whenever code is pushed to the `main` branch.

### Security Controls

#### Bandit

Performs static analysis of Python code to identify common security issues.

Example findings:

- Command injection
- Hardcoded credentials
- Weak cryptography usage
- Unsafe deserialization

---

#### Trivy

Scans the repository filesystem for:

- Vulnerable dependencies
- Misconfigurations
- Secrets

Severity threshold:

```text
HIGH
CRITICAL
```

---

#### Gitleaks

Detects accidentally committed secrets such as:

- API keys
- Tokens
- Passwords
- Cloud credentials

---

## Future Improvements

Possible enhancements include:

- Adding unit tests with pytest
- Dependency analysis with pip-audit
- Software Bill of Materials generation
- Container image scanning
- SAST with Semgrep
- DAST testing with OWASP ZAP
- Docker image hardening
- Multi-stage Docker builds

---

## Technologies Used

- Python 3.11
- Flask
- Docker
- GitHub Actions
- Bandit
- Trivy
- Gitleaks

---

## Learning Outcomes

This project demonstrates practical skills in:

- Secure coding
- DevSecOps
- CI/CD security
- Secret management
- Vulnerability detection
- Container security
