from fastapi import FastAPI,APIRouter,Depends,HTTPException,status
from app.database import get_db
from sqlalchemy.orm.session import Session
from app.models import Movie
from app.schemas import MovieResponce,MovieAdd,MovieUpdate
from typing import List
from app.oauth2 import get_current_user



router= APIRouter(prefix="/movies",tags=["Movies"])

@router.get("/",response_model=List[MovieResponce])
def movies(db:Session=Depends(get_db)):
    movies=db.query(Movie).all()
    return movies
@router.post("/",response_model=MovieResponce)
def add_movie(movie:MovieAdd,db:Session=Depends(get_db),user=Depends(get_current_user)):
    new_movie=Movie(**movie.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie
@router.patch("/{id}")
def update_movie(id:int,movie:MovieUpdate,db:Session=Depends(get_db),user=Depends(get_current_user) ):
    movie_query=db.query(Movie).filter(Movie.id==id)
    old_movie=movie_query.first()
    if not old_movie:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid movie id")
    updated=movie_query.update(movie.dict(),synchronize_session=False)
    db.commit()
    return movie_query.first()
@router.delete("/{id}")
def delete_movie(id:int,db:Session=Depends(get_db),user=Depends(get_current_user)):
    movie_query=db.query(Movie).filter(Movie.id==id)
    if not movie_query.first():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid movie id")
    movie_query.delete(synchronize_session=False)
    db.commit()
    return  {"message":"the movie was successfully deleted"}





    
    