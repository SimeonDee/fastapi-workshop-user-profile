# fastapi-workshop-user-profile

A walkthrough of FastAPI for building RESTful application, a practical demonstration I used for my students at a workshop.

## Contact

- `Adedoyin Simeon Adeyemi` | [LinkedIn](https://www.linkedin.com/in/adedoyin-adeyemi-a7827b160/)

## Setup

### Creat virtual environment

```bash
~ $ python -m venv .venv
```

### Activate virtual environment

- (Mac users)

```bash
~ $ source .venv/bin/activate
```

- (Windows users)

```bash
~ $ .venv/Scripts/activate.bat
```

### Install dependencies

```bash
(.venv) ~ $ pip install -r requirements.txt
```

### Start MySQL Database Server

- Install MySql Database and start the service
- Create Database
- Set the following variable values as (DB_HOST, DB_PORT, DB_USERNAME, DB_PASSWORD, DB_NAME) as environment variable

### Run application

- Locally (debug mode)

```bash
(.venv) ~ $ uvicorn src/main:app --reload --port 8000
```

- Production (You can set a port to be exposed if using a Docker container)

```bash
(.venv) ~ $ uvicorn src/main:app --host 0.0.0.0 --port 8000
```

## Tools Used

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- Python-dotenv
- PyMysql (DB Connector)
- uv (Package manager)
- MySQL (DBMS)
