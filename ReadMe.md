# Metrics collection system using Grafana

This project allows you to start collecting metrics for your project using grafana and graphite browser.
In the project you can find two basic examples on how to collect data using graphite and MySQL.
```bash
inserter.py
```
&
```bash
statsd_inserted.py
```
are two examples that you can use as a reference for your metrics collection

## Installation

### Prerequisites

* docker
* python3
* sudo rights
* internet access

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r ./requirements.txt
```

## Usage

Start the system
```bash
cd ./docker_containers
sudo docker-compose up -d
```

Stop the system
```bash
cd ./docker_containers
docker-compose down
```

Insert data into graphite/grafana
```bash
python3 statsd_inserted.py
```
Insert data into mysql
```bash
python3 inserter.py
```

## !!! Warining !!!

Be aware that this is en exapmle to use within the local network in case you want to deploy it to publicly availible hosts make sure to replace hardcoded credentials with environment variables.