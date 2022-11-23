# Fibonnaci Tool (Docker, Django, and NGINX)


## Building/Running the Application Through Docker
enter command below to docker terminal
```
docker-compose up --build -d
```

## Building the Application Through .venv
```
python -m venv ./backend/.venv
. ./initVenv.sh
pip install -r ../requirements.txt
```

## Running the app 
Ensure first if your (.venv) is activated and your in the /backend directory, 
by executing this in your terminal
```
. ./initVenv.sh
```

But if you're already in the /backend directory, execute this instead
```
. .venv/Scripts/activate
```

Then enter 127.0.0.1:8000 or localhost:8000 into the browser

## Fibonacci API Endpoints
#### Creating Fibonacci
Endpoint: 127.0.0.1:8000/api/fibonacci/

Request-type: POST

Request body content:

```
{
    "n": 1
}
```

#### Retrieving all list
Endpoint: 127.0.0.1:8000/api/fibonacci/

Request-type: GET

#### Retrieving specific fibonacci by ID
Endpoint: 127.0.0.1:8000/api/fibonacci/:ID

Request-type: GET
