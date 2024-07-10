# priobike-logs-study

This repository contains scripts to gather and check logs from our backend services. We developed those to check, if the logs contain any confidential or sensitive information.

[Learn more about PrioBike](https://github.com/priobike)

## Quickstart

### Gather Docker Service Logs

Create the following directory structure on the VM.
```
log_study/logs
          |- docker (directory for the docker logs)
          |- nginx (directory for the nginx logs)
```

Create/Copy the `fetch.py` file to the VM in the follwing directory.
```
log_study/fetch.py
```

Fetch logs via the following command. Must be executed on the VM.
```bash
python3 fetch.py
```

Download the logs via the following command. Must be executed on the local machine.
```bash
    scp 'USERNAME@SERVER:/<PATH>/log_study/logs/docker/*' logs/docker/
```

### Gather Nginx Logs

This instructions are only valid if the Nginx logs are written to files. Copy the logs to a new directory (where we have appropriate permissions) via the following command. Must be executed on the VM.
```bash
sudo cp /var/log/nginx/* /<PATH>/log_study/logs/nginx/
```

Download the logs via the following command. Must be executed on the local machine.
```bash
scp 'USERNAME@SERVER:/<PATH>/log_study/logs/nginx/*' logs/nginx/
```

Extract the .gz files via the following command. Must be executed on the local machine.
```bash
gunzip logs/nginx/*.gz
```

### Check logs

Check the logs via the following command. Must be executed on the local machine.
```bash
python3 check_logs.py
```
## Contributing

We highly encourage you to open an issue or a pull request. You can also use our repository freely with the `MIT` license.

Every service runs through testing before it is deployed in our release setup. Read more in our [PrioBike deployment readme](https://github.com/priobike/.github/blob/main/wiki/deployment.md) to understand how specific branches/tags are deployed.

## Anything unclear?

Help us improve this documentation. If you have any problems or unclarities, feel free to open an issue.
