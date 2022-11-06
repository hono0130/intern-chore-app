from sqlalchemy import create_engine

from models.model import Base

import os

DB_URL = "postgresql://ewouccfybcpusn:129a6be4478493115e46b969f5c3925a8c91650dfef1555505470ea8c49ba361@ec2-34-239-241-121.compute-1.amazonaws.com:5432/dd01v6ev0tbt0"
engine = create_engine(DB_URL, echo=True)

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    reset_database()
