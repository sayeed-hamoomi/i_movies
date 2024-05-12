from pydantic import BaseModel
from typing import Optional


class MovieBase(BaseModel):
    title:str
    discreption:str
    year:int
class MovieResponce(MovieBase):
    id:int
class MovieAdd(MovieBase):
    pass
class MovieUpdate(BaseModel):
    title:Optional[str]
    discreption:Optional[str]
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


        


