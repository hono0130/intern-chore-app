from http.client import HTTPException
from typing import List, Tuple, Dict, Union
from xmlrpc.client import DateTime, boolean
from models import model
import models
from db import session

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import and_
import schemas.chores as chore_schema

# Create
def create_chore(userID: int, chore_create: chore_schema.ChoreCreate):
    chore = model.Chore()
    chore.name = chore_create.chore_name
    chore.category = chore_create.cat
    chore.frequency = chore_create.frequency
    chore.user_id = userID

    session.add(chore)
    session.commit()
    session.close

    history = model.History()
    history.finish = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    history.chore_id = chore.chore_id

    session.add(history)
    session.commit()
    session.close()

def timestamp_create(choreID: int, stamp: chore_schema.choreTimeStamp):
    history = model.History()
    history.chore_id = choreID
    history.start = stamp.start
    history.finish = stamp.finish

    session.add(history)
    session.commit()
    session.close()

# Read
def get_all_chores(
    userID,
) -> Dict[str, Dict[str, Union[str, boolean, datetime.timedelta]]]:
    chores = session.query(model.Chore).filter(model.Chore.user_id == userID).all()
    chore_dict = {}
    for i in range(len(chores)):
        chore = chores[i]
        key = chore.chore_id
        value = {}
        value["name"] = chore.name
        value["category"] = chore.category
        value["frequency"] = chore.frequency

        history = (
            session.query(model.History)
            .filter(model.History.chore_id == chore.chore_id)
            .first()
        )
        print(key)
        print(history)
        value["finish"] = history.finish
        chore_dict[key] = value

    return chore_dict

def authorize_chore(userID: int, choreID: int):
    if not session.query(model.Chore).filter(model.Chore.user_id==userID).filter(model.Chore.chore_id==choreID).all():
        raise HTTPException(status_code=404, detail="task_not_found")


# Update
def update(
    userID: int, choreID: int, chore_info: chore_schema.ChoreCreate
) -> None:
    chore = (
        session.query(model.Chore)
        .filter(model.Chore.user_id == userID)
        .filter(model.Chore.chore_id == choreID)
        .first()
    )
    chore.name = chore_info.chore_name
    chore.category = chore_info.cat
    chore.frequency = chore_info.frequency
    session.commit()
    session.close()

    return chore


# Delete
def delete_chore(userID: int, choreID: int):
    chore = (
        session.query(model.Chore)
        .filter(and_(model.Chore.user_id == userID, model.Chore.chore_id == choreID))
        .first()
    )
    session.delete(chore)
    session.commit()
    session.close()

    history = (
        session.query(model.History).filter(model.History.chore_id == choreID).all()
    )

    for deletedata in history:
        print(deletedata)
        session.delete(deletedata)
        session.commit()

    session.close()

