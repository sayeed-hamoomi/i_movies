from fastapi import FastAPI,APIRouter,Depends
from app.database import get_db
from sqlalchemy.orm.session import Session
from app.models import Movie
from app.schemas import MovieResponce,MovieAdd
from typing import List
from app.oauth2 import get_current_user



router= APIRouter()

@router.get("/movies",response_model=List[MovieResponce])
def movies(db:Session=Depends(get_db)):
    movies=db.query(Movie).all()
    return movies
@router.post("/movies",response_model=MovieResponce)
def add_movie(movie:MovieAdd,db:Session=Depends(get_db),user=Depends(get_current_user)):
    new_movie=Movie(**movie.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie



    
    