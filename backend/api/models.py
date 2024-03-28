from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from .database import engine
Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"
    id=Column(Integer,primary_key=True,index=True)
    task=Column(String)
    completed=Column(Boolean,default=False)

Base.metadata.create_all(bind=engine)