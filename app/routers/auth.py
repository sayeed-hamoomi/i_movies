from fastapi import APIRouter,Depends,HTTPException,status
from app.database import get_db
from sqlalchemy.orm.session import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.models import User
from app.utils import verify_password
from app.oauth2 import create_access_token

router=APIRouter()

@router.post("/login")
def userlogin(authpayload:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(User).filter(User.username==authpayload.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid credential")
    if not verify_password(authpayload.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid credential")
    token=create_access_token({"user_id":user.id})
    return{"access_token":token,"token_type":"Bearer"}
    


    


