from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from  sqlalchemy.orm import Session
from ..database import db
from ..schemas.user_schemas import UserLogin,UserCreate
from ..controllers.auth_controllers import authenticate_user,create_user

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)



@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user:UserCreate, db: Session = Depends(db.get_db)):
    return create_user(user,db)


@router.post("/login", status_code=status.HTTP_200_OK)   
def login_user(user:UserLogin, db: Session = Depends(db.get_db)):
    return authenticate_user(user.email,user.password,db)