from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import engine, Base
from . import models, crud, schemas
from .deps import get_db

app = FastAPI(title="Todo Microservice")

Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/todos", response_model=List[schemas.TodoRead])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip=skip, limit=limit)
    return todos

@app.get("/todos/{todo_id}", response_model=schemas.TodoRead)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = crud.get_todo(db, todo_id=todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.post("/todos", response_model=schemas.TodoRead)
def create_todo(todo_in: schemas.TodoCreate, db: Session = Depends(get_db)):
    todo = crud.create_todo(db, todo_in=todo_in)
    return todo

@app.patch("/todos/{todo_id}", response_model=schemas.TodoRead)
def update_todo(todo_id: int, todo_in: schemas.TodoUpdate, db: Session = Depends(get_db)):
    todo = crud.update_todo(db, todo_id=todo_id, todo_in=todo_in)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_todo(db, todo_id=todo_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Todo not found")
    return None