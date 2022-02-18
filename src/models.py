import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
# from enum import Enum

Base = declarative_base()


class MediaType(Enum):
        VIDEO = 1
        PICTURE = 2

class Follower(Base):
    __tablename__ = 'follower'
    user_from_ID = Column(Integer, primary_key=True)  
    user_to_ID =  Column(Integer, primary_key=True)  


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, nullable=False)
    comment_text = Column(String(400))
    author_id = Column(Integer(), primary_key=True)
    post_id = Column(Integer, ForeignKey('Post.id'))


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True, nullable=False)
    media_type = Column(Enum(MediaType))  
    url = Column(String())
    post_id = Column(Integer, ForeignKey('Post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    create_at = Date()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, ForeignKey('Follower.User_from_ID'))
    username = Column(String(), primary_key=True, unique=True, nullable=False)
    name = Column(String(200))
    email = Column(String(40), nullable=False)
    author_id = relationship("Comment", backref="user")
    user_to_ID = relationship("Follower", uselist=False)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise 

