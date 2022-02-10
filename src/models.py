import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
from enum import Enum

Base = declarative_base()

class MediaType(Enum):
        VIDEO = 1
        PICTURE = 2

class Follower(Base):
    __tablename__ = 'follower'
    User_from_ID = Column(Integer, primary_key=True)  
    User_to_ID =  Column(Integer, primary_key=True)  


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, nullable=False)
    comment_text = Column(String(400))
    author_id = Column(Integer(20), primary_key=True)
    post_id = Column(Integer, ForeignKey('Post.id'))


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, nullable=False)
    media_type = Column(Enum(MediaType))  
    url = Column(String())
    post_id = Column(Integer, ForeignKey('Post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    create_at = Column(Date(dd/mm/yy))

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeignKey('Follower.User_from_ID', 'Follower.User_to_ID', 'Comment.author_id'))
    username = Column(String(), nullable=False)
    name = Column(String(200))
    email = Column(String(40), nullable=False)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise 