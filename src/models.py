import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Comment (Base):
    __tablename__="comment"
    ID = Column(Integer, primary_key = True)
    comment_text=Column(String(500))
    author_id= Column(Integer, ForeignKey("user.id"))
    post_id= Column(Integer, ForeignKey("post.id"))


class Post (Base):
    __tablename__="post"
    ID = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey("user.id"))

class Media(Base):
    __tablename__="media"
    ID = Column(Integer, primary_key = True)
    type = (String(25))
    url = (String(2083)) #Si usamos Internet Explorer
    post_id = Column(Integer, ForeignKey("post.id"))

class Follower(Base):
    __tablename__="follower"
    ID = Column(Integer, primary_key=True)
    user_from_id= Column(Integer, ForeignKey("user.id"))
    user_to_id= Column(Integer, ForeignKey("user.id"))

class User(Base):
    __tablename__="user"
    ID = Column(Integer, primary_key=True)
    username = Column(String(25), nullable=False, unique = True)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25))
    password = Column (String(16), nullable=False)
    email = Column(String(150), nullable=False, unique = True)




# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
