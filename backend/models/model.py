from datetime import datetime
from this import s
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Interval, Boolean
from sqlalchemy.orm import relationship

from db import Engine
from db import Base

class User(Base):
    """
    ユーザモデル
    """

    __tablename__ = 'users'
    __table_args__ = {
        'comment': 'ユーザー情報のテーブル'
    }

    user_id = Column('user_id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(200))
    email = Column('email', String(100), unique=True)
    password = Column('password', String(100))
    layout = Column('layout', String(100))
    gender = Column('gender', String(100))
    birthday = Column("birthday", DateTime)

class Chore(Base):
    """
    家事モデル
    """
    __tablename__ = 'chores'
    __table_args__ = {
        'comment': '家事情報のテーブル'
    }
    chore_id = Column('chore_id', Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer, ForeignKey('users.user_id'))
    name = Column('name', String(200))
    category = Column('category', String(200))
    frequency = Column('frequency', Integer)

class History(Base):
    __tablename__ = 'histories'
    __table_args__ = {
        'comment': '家事履歴のテーブル'
    }
    dummy_id = Column('dummy_id', Integer, primary_key=True, autoincrement=True)
    chore_id = Column('chore_id', Integer, ForeignKey('chores.chore_id'))
    start = Column('start', String(200))
    finish = Column('finish', String(200))

class LineUser(Base):
    __tablename__ = 'line_users'
    __table_args__ = {
        'comment': 'lineidとemailの対応'
    }
    line_id = Column("line_id", String(200), primary_key=True)
    email = Column("email", String(100), ForeignKey('users.email'))
