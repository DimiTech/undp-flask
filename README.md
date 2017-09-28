# UNDP Form Service

## How to run it:

```
make
```

## Test the app:

```
curl -i -X GET http://127.0.0.1:5000
curl -i -X POST \
-H 'Content-Type: application/json' \ 
-d @example_open_data.json \
http://127.0.0.1:5000
```

## Project structure:

```
/
|-- docker-compose.yml
|-- Makefile
|-- README.md
|-- app/    # All the application code lives here.
|-- static/ # Static files served by nginx.
`-- SQL/
    `-- docker-entrypoint-initdb.d/ # Contains DB initialization scripts.
```

## DB Migrations:
```
cd ./app
# Run only once:
# FLASK_APP=main.py flask db init
FLASK_APP=main.py flask db migrate
FLASK_APP=main.py flask db upgrade
```
