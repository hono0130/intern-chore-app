from typing import Optional, Union
import datetime

from pydantic import BaseModel, Field
from sqlalchemy import true

# Request


class ChoreCreate(BaseModel):
    frequency: int
    chore_name: Optional[str] = Field(None, example="掃除機をかける")
    cat: Optional[str] = Field(None, example="そうじ")

    class Config:
        orm_mode = True

class choreTimeStamp(BaseModel):
    start: str
    finish: str
    

class ChoreResponse(BaseModel):
    chore_dict: dict[int, dict[str, Union[str, datetime.timedelta]]] = Field(
        example={
            "1": {
                "name": "掃除機をかける",
                "is_todo": True,
                "category": "掃除",
                "timedelta": datetime.timedelta(days=3).days,
            }
        }
    )

