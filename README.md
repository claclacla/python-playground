# Python playground

--------------------------------------------------------------------------------

### Prerequisites

What things you need to install the software

```
docker 17+
docker-compose 1.19.0+
```

--------------------------------------------------------------------------------

### Installing

#### Python3

```
# Pull the python image
sudo docker pull python:3.6-slim

# Change the directory to the playground folder
cd path-to-your-playground

# Create a .env file with your local playground folder
echo "APP_FOLDER=/path-to-your-playground" > .env

```

--------------------------------------------------------------------------------

### Executing

#### Python3

```
# Run the python environment
sudo docker-compose -f docker/docker-compose.yaml up -d

# Execute your python scripts ...
sudo docker exec -it PythonPlayground bash

# Execute your python scripts ...

```

--------------------------------------------------------------------------------

## Authors

- **Simone Adelchino** - [github](https://github.com/claclacla)
