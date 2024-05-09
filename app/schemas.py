from pydantic import BaseModel


class MovieBase(BaseModel):
    title:str
    discreption:str
    year:int
class MovieResponce(MovieBase):
    id:int
class MovieAdd(MovieBase):
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


        


