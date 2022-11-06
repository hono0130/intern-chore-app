
from operator import imod
from typing import List, Tuple, Dict, Union
from xmlrpc.client import DateTime, boolean
from schemas.chores import ChoreCreate
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
import cruds.chores as chore_crud
import datetime

import schemas.chores as chore_schema
from auth import get_current_user
from models.model import User

from cruds.chores import get_all_chores, delete_chore, create_chore, timestamp_create, update,  timestamp_create, authorize_chore


router = APIRouter()

@router.post("/chore/create")
def create_new_chore(chores: chore_schema.ChoreCreate, current_user: User = Depends(get_current_user)):
    """
    家事の新規登録
    フォームからデータベースに格納

    Args:
        userID (int): ユーザーIDをURIから取得
        chores (chore_schema.ChoreCreate): 家事の情報をフォームから取得
    """
    create_chore(userID=current_user.user_id, chore_create=chores)


@router.delete("/{choreID}/delete")
def delete(choreID: int, current_user: User = Depends(get_current_user)):
    return  delete_chore(current_user.user_id, choreID)

@router.put("/{choreID}/update")
def update_chore(choreID: int, chore_info: chore_schema.ChoreCreate, current_user: User = Depends(get_current_user)):
    """
    登録した家事の更新

    Args:
        choreID (int): 家事IDをURIから取得
    """
    chore = update(current_user.user_id, choreID, chore_info)
    return chore


@router.get("/top", response_model=Dict[str, Dict[str, Union[str, boolean, datetime.timedelta]]])
async def show_chore(current_user: User = Depends(get_current_user)):
    """
    ユーザーIDから全てのChoreIDを取得
    choreIDから全ての家事の最新のデータを取得
    {{1: {name: 掃除機をかける, is_todo: True, timedelta: 3, category:掃除}}

    Args:
        userID (int): ユーザーIDをURIから取得
    """

    chore_dict = get_all_chores(current_user.user_id)
    
    processed_dict = {}

    for key, dic in chore_dict.items():
        a_dict = {}

        finish = datetime.datetime.strptime(dic["finish"], '%Y-%m-%d %H:%M:%S')
        frequency = datetime.timedelta(days=dic["frequency"])
        today = datetime.datetime.now()

        if (today - finish) >= frequency:
            a_dict["is_todo"] = True
        
        else:
            a_dict["is_todo"] = False

        a_dict["timedelta"] = ((today - finish).seconds / 3600)
        a_dict["name"] = dic["name"]
        a_dict["category"] = dic["category"]

        processed_dict[key] = a_dict

    return processed_dict

@router.post("/{choreID}/timestamp", response_model=None)
def create_timestamp(choreID: int, stamp: chore_schema.choreTimeStamp, current_user: User = Depends(get_current_user)):
    authorize_chore(current_user.user_id, choreID)
    timestamp_create(choreID, stamp)
