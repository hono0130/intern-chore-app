from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import psycopg2



import os

# 接続先DBの設定
DATABASE = "postgresql://ewouccfybcpusn:129a6be4478493115e46b969f5c3925a8c91650dfef1555505470ea8c49ba361@ec2-34-239-241-121.compute-1.amazonaws.com:5432/dd01v6ev0tbt0"

# Engine の作成

Engine = create_engine(
  DATABASE,
  convert_unicode=True,
  echo=True
)

# Sessionの作成
session = scoped_session(
    sessionmaker(
      autocommit = False,
	    autoflush = False,
	    bind = Engine
    )
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()

def init_db():
    #assetsフォルダのmodelsをインポート
    import models.model
    Base.metadata.create_all(bind=Engine)

