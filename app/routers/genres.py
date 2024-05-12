from fastapi import APIRouter,Depends,HTTPException,status
from app.database import get_db
from app.models import Genre,Role
from sqlalchemy.orm.session import Session
from typing import List
from app.schemas import GenreBase,GenreResponse,AddGenre
from app.oauth2 import get_current_user


router=APIRouter(prefix="/genres",tags=["Genres"])

@router.get("/",response_model=List[GenreResponse])
def genres(db:Session=Depends(get_db)):
    genres=db.query(Genre).all()
    return genres
@router.post("/",response_model=GenreResponse)
def add_genre(genre:AddGenre,db:Session=Depends(get_db),user=Depends(get_current_user)):
    if user.role != Role.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="admin only")
    new_genre=Genre(**genre.dict())
    db.add(new_genre)
    db.commit()
    db.refresh(new_genre)
    return new_genre
@router.delete("/{id}")
def delete_genre(id:int,db:Session=Depends(get_db),user=Depends(get_current_user)):
    if user.role != Role.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="admin only")
    genre_query=db.query(Genre).filter(Genre.id==id)
    if not genre_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="id does not match")
    
    genre_query.delete(synchronize_session=False)
    db.commit()
    return {"messege":"the genre is successfull deleted"}