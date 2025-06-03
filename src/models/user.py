from sqlalchemy import Table, Column, Integer, String

from src.config.db import meta, conn

Users = Table(
    "users", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(250)),
    Column("email", String(250), unique=True, nullable=False),
    Column("password", String(250), nullable=False)
)

Users.create(bind=conn, checkfirst=True)