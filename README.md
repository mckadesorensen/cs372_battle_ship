# cs372_battle_ship ![Build Status](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoibHVqQlI4RjVkUTJ1Snc1T2N6UHhHZTNKbWpWMWhkdVFxVGlFQTF2NGZtRENJQ1B1UEp4a0FZc3NOQkJackZGUHR0UG9iZzdGRTFoSEtPY1BCS2lNaEk4PSIsIml2UGFyYW1ldGVyU3BlYyI6IjhPcXJlUWVGY3JYQXpyaE0iLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=master)

## Table of Content 

- [Docker](#Docker)
    - [Building Docker](#Building-Docker)
    - [Running Docker](#Running-Docker)
- [Unit Tests](#Unit-test)
    - [Running Unit Tests](#Running-Unit-Tests)
 
 
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
Copy the most recent `IMAGE ID` and run the following command:
```terminal
docker run -it 3bc811affb74
```

## Unit Tests
This project uses [pytest](https://docs.pytest.org/en/latest/).

### Running Unit Tests
After running the [Docker](#Running-Docker) run command, run this command in the `Docker container`:
```Terminal
pipenv run tests
``` 
This command is created in the `[scripts]` section in Pipfile.






