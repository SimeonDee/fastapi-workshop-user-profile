import os

from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", 3306)  # defaults to mysql port
DB_USERNAME = os.getenv("DB_USERNAME", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "localhost")
DB_NAME = os.getenv("DB_NAME")

conn_str = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}" # noqa

meta = MetaData()

engine = create_engine(conn_str)
conn = engine.connect()
