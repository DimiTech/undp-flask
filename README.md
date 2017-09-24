# UNDP Form Service

## How to run it:

```
make
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
