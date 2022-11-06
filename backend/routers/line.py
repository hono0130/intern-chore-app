from fastapi import APIRouter

import schemas.line as line_schema
from cruds.line import create_line_id, create_start_stamp, read_chore_id, userID_from_lineID, read_all_chores, update_timestamp, read_chore_id_fin

router = APIRouter()

@router.post("/line_id")
def get_line_id(line_id: line_schema.LineID):
    create_line_id(line_id)

@router.get("/line/chores")
def get_all_chores(line_id: line_schema.LineBase):
    
    user_id = userID_from_lineID(line_id.line_id)
    chores = read_all_chores(user_id)

    chore_dic = {}
    for i  in range(len(chores)):
        chore_dic[i] = chores[i].name
    
    return chore_dic

@router.post("/start")
def start(time: line_schema.StartTime):
    user_id = userID_from_lineID(time.line_id)
    chore_id = read_chore_id(time, user_id)
    create_start_stamp(time, chore_id)

@router.post("/finish")
def finish(time: line_schema.FinishTime):
    user_id = userID_from_lineID(time.line_id)
    chore_id = read_chore_id_fin(time, user_id)
    dic = update_timestamp(time, chore_id)
    dic["name"] = time.name
    return dic