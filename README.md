# UNDP Form Service

## How to run it:

```
make
```

Wait for a minute after all the containers are started in order for them to run
their applications.

## Test the app:

Go to:

```
http://localhost/
```

and fill in and submit the form.

If the request was successful you should be redirected to a "sucess" page,
with the `id` query parameter containing the UUID of the newly created record.

## Project structure:

```
/
|-- docker-compose.yml
|-- Makefile
|-- README.md
|-- app/    # Main application code.
    `-- db/ # Database initialization and Models.
|-- static/ # Static pages served by nginx.
```

## DB Migrations:
```
cd ./app
# Run only once:
# FLASK_APP=main.py flask db init
FLASK_APP=main.py flask db migrate
FLASK_APP=main.py flask db upgrade
```
