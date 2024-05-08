from pydantic import BaseModel


class MovieBase(BaseModel):
    title:str
    discreption:str
    year:int
class MovieResponce(MovieBase):
    id:int   


