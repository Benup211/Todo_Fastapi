from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"
engine=create_engine(SQLALCHEMY_DATABASE_URL,echo=True,connect_args={"check_same_thread":False})
session=sessionmaker(autocommit=False,autoflush=False,bind=engine)()