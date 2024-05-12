from fastapi import APIRouter,Depends,HTTPException,status
from app.database import get_db
from sqlalchemy.orm.session import Session
from typing import List
from app.models import Director,Role
from app.schemas import DirectorResponse,AddDirector
from app.oauth2 import get_current_user

router= APIRouter(prefix="/directors",tags=["Directors"])


@router.get("/")
def directors(db:Session=Depends(get_db)):
    directors=db.query(Director).all()
    return directors
@router.post("/",response_model=DirectorResponse)
def create_director(director:AddDirector,db:Session=Depends(get_db),user=Depends(get_current_user)):
    if user.role != Role.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="admin only")
    new_director=Director(**director.dict())
    db.add(new_director)
    db.commit()
    db.refresh(new_director)
    return new_director
@router.delete("/{id}",response_model=DirectorResponse)
def delete_director(id:int,db:Session=Depends(get_db),user=Depends(get_current_user)):
    if user.role != Role.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="admin only")
    director_query=db.query(Director).filter(Director.id==id)
    if not director_query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="id does not match with director")
    director_query.delete(synchronize_session=False)
    db.commit()
    return {"messege":"the director was successfully deleted"}