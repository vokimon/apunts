from fastapi import FastAPI
import schemas
app = FastAPI()

from database import engine, SessionLocal, Base
from sqlalchemy.orm import Session

fakeDatabase = {
    0: {'task': "task 0"},
    1: {'task': "task 1"},
    2: {'task': "task 2"},
    3: {'task': "task 3"},
}

Base.metadata.create_all(engine)



@app.get('/')
def get_items():
    return fakeDatabase


@app.get('/{id}')
def get_item(id: int):
    return fakeDatabase[id]

@app.post('/')
def add_item(item: schemas.Item):
    """
    Adds a peding task
    """
    new_id = len(fakeDatabase)
    fakeDatabase[new_id] = item
    return fakeDatabase

"""
@app.post('/')
def add_item(item: Body()):
    new_id = len(fakeDatabase)
    fakeDatabase[new_id] = item
    return fakeDatabase
"""

@app.put('/{id}')
def update_item(id: int, item: schemas.Item):
    fakeDatabase[id]['task'] = item.task
    return fakeDatabase

@app.delete('/{id}')
def update_item(id: int):
    del fakeDatabase[id]
    return fakeDatabase

