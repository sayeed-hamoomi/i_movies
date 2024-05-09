from jose import JWTError, jwt
from app.config import settings
from datetime import datetime,timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from app.database import get_db
from sqlalchemy.orm.session import Session
from app.models import User


secret_key=settings.secret_key
algorithm=settings.algorithm
access_expire_minutes=settings.access_expire_minutes

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=access_expire_minutes)
    to_encode.update({"exp":expire})
    token=jwt.encode(to_encode,secret_key,algorithm)
    return token
def verify_access_token(token:str,credential_exception):
    try:
        token_data=jwt.decode(token=token,key=secret_key,algorithms=[algorithm])
    except JWTError:
        raise credential_exception
    user_id=token_data.get("user_id")
    if not user_id:
        raise credential_exception
    return user_id
def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
    credential_exception= HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="invalid token")
    user_id= verify_access_token(token=token,credential_exception=credential_exception)
    user=db.query(User).filter(User.id==user_id).first()
    if not user:
        raise credential_exception
    return user




    

