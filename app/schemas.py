from pydantic import BaseModel
from typing import Optional,List


class MovieBase(BaseModel):
    title:str
    description:str
    year:int
class MovieResponce(MovieBase):
    id:int

class MovieResponse(BaseModel):
    Movie:MovieResponce
    genre_id:int

    class Config:
        from_attributes = True
    
class MovieAdd(MovieBase):
    genres:List[int]
class MovieUpdate(BaseModel):
    title:Optional[str]
    description:Optional[str]
    year:Optional[str]


class GenreBase(BaseModel):
      genre_name:str
class GenreResponse(GenreBase):
    id:int
class AddGenre(GenreBase):
    pass

class DirectorBase(BaseModel):
    director_name:str
class DirectorResponse(DirectorBase):
    id:int
class AddDirector(DirectorBase):
    pass


class UserBase(BaseModel):
    username:str
    password:str
    role:str
class UserCreate(BaseModel):
    username:str
    password:str
    role:str    
class UserResponse(UserBase):
    id:int


        


