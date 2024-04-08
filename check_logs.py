import os
import re
import random

def check_ip_addresses(content):
    ip_addresses = re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", content)
    if ip_addresses and len(ip_addresses) > 0:
        if len(ip_addresses) > 5:
            # Get 5 random IP addresses
            ip_addresses = random.sample(ip_addresses, 5)
        print(f"IP addresses found (first five at max): {ip_addresses}")
        
def check_user_ids(content):
    if "[#" in content:
        user_ids = re.findall(r"\[#\d+\]", content)
        if user_ids and len(user_ids) > 0:
            if len(user_ids) > 5:
                # Get 5 random user IDs
                user_ids = random.sample(user_ids, 5)
            print(f"User IDs found (first five at max): {user_ids}")
            
def check_shortcuts(content):
    if "waypoint" in content:
        print("Waypoint found")
        
def check_log_files(log_dir):
    log_files = os.listdir(log_dir)
    for log_file in log_files:
        print(f"Checking log file: {log_file}")
        try:
            with open(f"{log_dir}/{log_file}", encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            with open(f"{log_dir}/{log_file}", encoding='cp1252') as f:
                content = f.read()
        check_ip_addresses(content)
        check_user_ids(content)
        check_shortcuts(content)

docker_log_dir = "logs/docker"
nginx_log_dir = "logs/nginx"

docker_log_files = os.listdir(docker_log_dir)
nginx_log_files = os.listdir(nginx_log_dir)

print("Checking logs")

check_log_files(docker_log_dir)
# check_log_files(nginx_log_dir)