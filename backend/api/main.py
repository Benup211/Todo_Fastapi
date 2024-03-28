from fastapi import FastAPI,status,Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .database import session
from .models import Todo
app=FastAPI()

origins=[
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)
class TodoSchema(BaseModel):
    task:str
    completed:bool=False

#welcome message
@app.get("/")
def read_root():
    return {"message":"This is a todo app"}

#read all todos
@app.get("/all")
def list_todos():
    todos=session.query(Todo).all()
    return todos
#post a todo
@app.post("/create")
async def create(todo:TodoSchema,response:Response):
    try:
        new_todo=Todo(task=todo.task,completed=todo.completed)
        session.add(new_todo)
        session.commit()
        return {"message":"Todo created successfully"}
    except Exception as e:
        response.status_code=status.HTTP_400_BAD_REQUEST
        return {"message":str(e)}    
#read a todo by id
@app.get("/todo/{id}")
def read(id:int,response:Response):
    todo=session.query(Todo).filter(Todo.id==id).first()
    if todo is None:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"message":"Todo not found"}
    return todo
#update a todo by id
@app.put("/update/{id}")
def update(id:int,todo:TodoSchema,response:Response):
    try:
        qtodo=session.query(Todo).filter(Todo.id==id).first()
        qtodo.task=todo.task
        qtodo.completed=todo.completed
        session.commit()
        return {"message":"Todo updated successfully"}
    except Exception as e:
        response.status_code=status.HTTP_400_BAD_REQUEST
        return {"message":str(e)}
#delete a todo by id
@app.delete("/delete/{id}")
def delete(id:int,response:Response):
    try:
        todo=session.query(Todo).filter(Todo.id==id).first()
        session.delete(todo)
        session.commit()
        return {"message":"Todo deleted successfully"}
    except Exception as e:
        response.status_code=status.HTTP_400_BAD_REQUEST
        return {"message":str(e)}