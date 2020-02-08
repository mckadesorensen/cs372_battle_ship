# cs372_battle_ship

## Table of Content 

- [Docker](#Docker)
    - [Building Docker](#Building-Docker)
    - [Running Docker](#Running-Docker)
    
 
 
## Docker
This project uses Docker. To install Docker visit this [link](https://docs.docker.com/install/) and follow your systems
instructions 

### Building Docker 
Run the following command within the project directory:
```terminal
docker build -f battleship.Dockerfile .
```
### Running Docker 
After [building Docker](#Building-Docker) run the following command:
```terminal
docker image ls
```
There should be a list of Docker images like below:
```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
<none>              <none>              3bc811affb74        1 minute ago       103MB
ubuntu              latest              ccc6e87d482b        3 weeks ago         64.2MB
```
Copy the most recent _IMAGE ID_ and run the following command:
```terminal
docker run -it 3bc811affb74
```




