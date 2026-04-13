from sqlalchemy.orm import Session

from . import models, schemas


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()

def get_todo(db: Session, todo_id: int) -> models.Todo | None:
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def create_todo(db: Session, todo_in: schemas.TodoCreate) -> models.Todo:
    db_todo = models.Todo(
        title=todo_in.title,
        description=todo_in.description,
        due_date=todo_in.due_date,
        status=todo_in.status,
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(
    db: Session, todo_id: int, todo_in: schemas.TodoUpdate
) -> models.Todo | None:
    db_todo = get_todo(db, todo_id=todo_id)
    if not db_todo:
        return None
    for field, value in todo_in.dict(exclude_unset=True).items():
        setattr(db_todo, field, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int) -> bool:
    db_todo = get_todo(db, todo_id=todo_id)
    if not db_todo:
        return False
    db.delete(db_todo)
    db.commit()
    return True