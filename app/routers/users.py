from fastapi import APIRouter,FastAPI,Depends
from app.database import get_db
from sqlalchemy.orm.session import Session
from app.models import User
from typing import List
from app.schemas import UserResponse,UserCreate
from app.utils import hash_password



router= APIRouter(prefix="/users",tags=["Users"])

@router.get("/",response_model=List[UserResponse])
def users(db:Session=Depends(get_db)):
    users=db.query(User).all()
    return users
@router.post("/",response_model=UserResponse)
def createuser(user:UserCreate,db:Session=Depends(get_db)):
    user.password= hash_password(user.password)
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
