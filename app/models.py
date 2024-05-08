from app.database import Base
from sqlalchemy import Column,Integer,String

class Movie(Base):
    __tablename__="movies"
    id=Column(Integer,primary_key=True)
    title=Column(String,nullable=False,unique=True)
    discreption=Column(String,nullable=False)
    year=Column(Integer,nullable=False)



