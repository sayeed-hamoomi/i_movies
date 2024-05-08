from fastapi import FastAPI,APIRouter,Depends
from app.database import get_db
from sqlalchemy.orm.session import Session
from app.models import Movie
from app.schemas import MovieResponce
from typing import List



router= APIRouter()

@router.get("/movies",response_model=List[MovieResponce])
def movies(db:Session=Depends(get_db)):
    movies=db.query(Movie).all()
    return movies
