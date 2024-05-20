from fastapi import FastAPI,APIRouter,Depends,HTTPException,status
from sqlalchemy.sql.functions import coalesce
from sqlalchemy import func
from app.database import get_db
from sqlalchemy.orm.session import Session
from app.models import Movie,Role,MovieGenre,Genre,MovieDirector,Director
from app.schemas import MovieResponce,MovieAdd,MovieUpdate, MovieResponse
from typing import List
from app.oauth2 import get_current_user
from sqlalchemy import or_



router= APIRouter(prefix="/movies",tags=["Movies"])

# @router.get("/")
@router.get("/",response_model=List[MovieResponse])
def movies(search:str="",page:int = 1,db:Session=Depends(get_db)):
    limit = 10
    skip = (page-1)*limit
    director_sub=db.query(Director.director_name).outerjoin(target=MovieDirector,onclause=Director.id==MovieDirector.director_id).filter(MovieDirector.movie_id==Movie.id).subquery()
    genre_sub = db.query(Genre.genre_name).outerjoin(target=MovieGenre,onclause=Genre.id==MovieGenre.genre_id).filter(MovieGenre.movie_id==Movie.id).subquery()
    movies=db.query(Movie,func.array(genre_sub).label("genres"),func.array(director_sub).label("directors")).filter(or_(Movie.title.icontains(search),Movie.description.icontains(search))).limit(limit).offset(skip).all()
   
    return movies
@router.post("/",response_model=MovieResponce)
def add_movie(movie:MovieAdd,db:Session=Depends(get_db),user=Depends(get_current_user)):
    if user.role != Role.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="admin only")
    md=movie.dict()
    del md["genres"]
    del md["directors"]
    new_movie=Movie(**md)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    for i in movie.genres:
        mg=MovieGenre(movie_id=new_movie.id,genre_id=i)
        db.add(mg)    
    for i in movie.directors:
        md=MovieDirector(movie_id=new_movie.id,director_id=i)
        db.add(md)
    db.commit()

    return new_movie
@router.patch("/{id}")
def update_movie(id:int,movie:MovieUpdate,db:Session=Depends(get_db),user=Depends(get_current_user) ):
    if user.role != Role.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="admin only")
    movie_query=db.query(Movie).filter(Movie.id==id)
    old_movie=movie_query.first()
    if not old_movie:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid movie id")
    updated=movie_query.update(movie.dict(),synchronize_session=False)
    db.commit()
    return movie_query.first()
@router.delete("/{id}")
def delete_movie(id:int,db:Session=Depends(get_db),user=Depends(get_current_user)):
    if user.role != Role.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="admin only")
    movie_query=db.query(Movie).filter(Movie.id==id)
    if not movie_query.first():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid movie id")
    movie_query.delete(synchronize_session=False)
    db.commit()
    return  {"message":"the movie was successfully deleted"}





    
    