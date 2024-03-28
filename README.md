# Gather Docker Service Logs

Create the following directory structure on the VM.
```
/home/admin/log_study/logs
                        |- docker
                        |- nginx
```

Create/Copy the `fetch.py` file to the VM in the follwing directory.
```
/home/admin/log_study/fetch.py
```

Fetch logs via the following command. Must be executed on the VM.
```bash
python3 fetch.py
```

Download the logs via the following command. Must be executed on the local machine.
```bash
scp 'admin@priobike.vkw.tu-dresden.de:/home/admin/log_study/logs/docker/*' logs/docker/  
```

# Gather Nginx Logs

Copy the logs to a new directory (where we have appropriate permissions) via the following command. Must be executed on the VM.
```bash
sudo cp /var/log/nginx/* /home/admin/log_study/logs/nginx/
```

Download the logs via the following command. Must be executed on the local machine.
```bash
scp 'admin@priobike.vkw.tu-dresden.de:/home/admin/log_study/logs/nginx/*' logs/nginx/
```

Extract the .gz files via the following command. Must be executed on the local machine.
```bash
gunzip logs/nginx/*.gz
```

# Check logs

Check the logs via the following command. Must be executed on the local machine.
```bash
python3 check_logs.py
```