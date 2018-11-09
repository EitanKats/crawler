# Simple Crawler

This is an explaination of how to use the crawler

## Installation

Make sure that you have docker installed.

First of all follow the readme in this [git](https://github.com/dperson/torproxy), after the container runs and works its time to install the crawler.

clone this repository.

There are a couple of ways to run this:

1. Using the docker run method in with the following syntax:
make sure you create the local dir

```bash
mkdir ~/data
docker run -e "DOCKER_HOST=$(ip -4 addr show docker0 | grep -Po 'inet \K[\d.]+')" -v ~/data:/crawler/data crawler
```

this sets the environmental variable DOCKER_HOST so that the code within the container uses the proxy that the Tor container provides.

Change the config.py so it matches the Tor docker port, and now build the image.


The configuration's default setting of the proxy is to localhost and port 9150.

You will need to change it to 9050 if u run the Tor docker with the following line

```bash
sudo docker run -it -p 8118:8118 -p 9050:9050 -d dperson/torproxy
```
2. running it manually:

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the packages.

remember to change configuration

run it with 
```bash
python main.py
```



## Run every Interval
This section is about running the crawler every given interval.
edit the /etc/crontab file and add the following line

```bash
*/1 * * * *  root /snap/bin/docker run -e "DOCKER_HOST=$(ip -4 addr show docker0 | grep -Po 'inet \K[\d.]+')" -v ~/data:/crawler/data  crawler
```
In the example above, it is set to run every 1 minute.

Remeber to reload cron configuration for it to run.

##

##
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.