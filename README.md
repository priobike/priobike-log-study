# Gather Docker Service Logs

Fetch logs via the following command. Must be executed on the VM.
```
python3 fetch.py
```

Download the logs via the following command. Must be executed on the local machine.
```
scp 'admin@priobike.vkw.tu-dresden.de:/home/admin/log_study/logs/docker/*' logs/docker/  
```

# Gather Nginx Logs

Copy the logs to a new directory (where we have appropriate permissions) via the following command. Must be executed on the VM.
```
sudo cp /var/log/nginx/* /home/admin/log_study/logs/nginx/
```

Download the logs via the following command. Must be executed on the local machine.
```
scp 'admin@priobike.vkw.tu-dresden.de:/home/admin/log_study/logs/nginx/*' logs/nginx/
```

Extract the .gz files via the following command. Must be executed on the local machine.
```
gunzip logs/nginx/*.gz
```

# Check logs

Check the logs via the following command. Must be executed on the local machine.
```
python3 check_logs.py
```