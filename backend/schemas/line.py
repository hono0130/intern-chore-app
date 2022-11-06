from pydantic import BaseModel, Field

class LineBase(BaseModel):
    line_id: str

    class Config:
        orm_mode=True


class LineID(LineBase):
    email: str

    class Config:
        orm_mode=True

class StartTime(LineBase):
    name: str
    start: str

class FinishTime(LineBase):
    name: str
    finish: str
