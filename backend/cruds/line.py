from db import session
import schemas.line as line_schema
from models.model import History, LineUser, User, Chore

from sqlalchemy import desc
# create

def create_line_id(line_id: line_schema.LineID):
    line_user = LineUser()
    line_user.line_id = line_id.line_id
    line_user.email = line_id.email

    session.add(line_user)

    try:  
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()  

def create_start_stamp(time: line_schema.StartTime, chore_id: int):
    history = History()
    history.chore_id =  chore_id
    history.start = time.start

    session.add(history)

    try:  
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()  

# read

def userID_from_lineID(line_id: str):

    line_user = session.query(LineUser).filter(LineUser.line_id == line_id).first()
    email = line_user.email
    user = session.query(User).filter(User.email == email).first()
    user_id = user.user_id
    
    session.close()

    return user_id

def read_all_chores(user_id: int):

    chores = session.query(Chore).filter(Chore.user_id == user_id).all()
    session.close()

    return chores

def read_chore_id(time: line_schema.StartTime, user_id: int):
    chore = session.query(Chore).filter(Chore.user_id == user_id).filter(Chore.name == time.name).first()
    return chore.chore_id

def read_chore_id_fin(time: line_schema.FinishTime, user_id: int):
    chore = session.query(Chore).filter(Chore.user_id == user_id).filter(Chore.name == time.name).first()
    return chore.chore_id


# update

def update_timestamp(time: line_schema.FinishTime, chore_id: int):
    history = session.query(History).filter(History.chore_id == chore_id).order_by(desc(History.dummy_id)).first()
    history.finish = time.finish

    dic = {"start": history.start, "finish": history.finish}

    try:  
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    
    return  dic
