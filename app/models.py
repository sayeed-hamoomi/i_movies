from app.database import Base
from sqlalchemy import Column,Integer,String,Enum,ForeignKey
from enum import Enum as PyEnum

class Role(PyEnum):
    ADMIN='admin'
    USER='user'

class Movie(Base):
    __tablename__="movies"
    id=Column(Integer,primary_key=True)
    title=Column(String,nullable=False,unique=True)
    discreption=Column(String,nullable=False)
    year=Column(Integer,nullable=False)


class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    username=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    role=Column(Enum(Role))

class Genre(Base):
    __tablename__="Genres"
    id=Column(Integer,primary_key=True)
    genre_name=Column(String,nullable=False,unique=True)

class Director(Base):
    __tablename__="directors"
    id =Column(Integer,primary_key=True)
    director_name=Column(String,nullable=False,unique=True)


class MovieGenre(Base):
    __tablename__="movies_genres"
    movie_id =Column(Integer,ForeignKey("movies.id",ondelete='CASCADE'),nullable=False,primary_key=True)
    genre_id =Column(Integer,ForeignKey("Genres.id",ondelete='CASCADE'),nullable=False,primary_key=True)
   


