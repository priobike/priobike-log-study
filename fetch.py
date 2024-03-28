import os
import json
from io import StringIO  
from time import sleep

import subprocess

LOGS_TAIL = 5000

print("Gathering running services")
cmd = ['docker', 'service', 'ls', '--format', '{{json . }}']
result = subprocess.run(cmd, capture_output=True, text=True)

# Parse the output into a list of dictionaries
result = [json.loads(line) for line in result.stdout.strip().split('\n')]

services = [service['Name'] for service in result]

print("Fetching logs for services")
for service in services:
    print(f"Service: {service}")
    cmd = ['docker', 'service', 'logs', '--tail', str(LOGS_TAIL), service]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        output = result.stdout + "\n\n" + result.stderr
    except subprocess.TimeoutExpired as e:
        print("Timeout")
        output = e.stdout + "\n\n" + e.stderr
    with open(f"logs/docker/{service}.log", "w") as f:
        f.write(output)