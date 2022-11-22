# Fibonnaci (Docker, Django and NGINX)

## Building the Project
enter command below to docker terminal
```
docker-compose up --build -d
```

## Running the app 
Enter 127.0.0.1:8000 browser to access

## Fibonacci API Endpoints
#### POST - Creating Fibonacci
endpoint: 127.0.0.1:8000/api/fibonacci/
request body content:

```
{
    "n": 1
}
```

#### GET - endpoint for retrieving all list
endpoint: 127.0.0.1:8000/api/fibonacci/

#### GET - Retrieving specific fibonacci by ID
endpoint: 127.0.0.1:8000/api/fibonacci/1