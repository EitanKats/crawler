# Simple Crawler

This is an explaination of how to use the crawler

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the packages.

First of all follow the readme in this [git](https://github.com/dperson/torproxy), after the container runs and works its time to install the crawler.

Now please clone the code from this repository.

There are a couple of ways to run this:

1. Using the docker run method in with the following syntax:

```bash
docker container run -e "DOCKER_HOST=$(ip -4 addr show docker0 | grep -Po 'inet \K[\d.]+')"
```

this sets the environmental variable DOCKER_HOST so that the code within the container uses the proxy that the Tor container provides.

2. Change the config.py set the proxy manually and build the image

##
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.