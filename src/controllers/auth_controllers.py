from ..errors import notfound,notauthorized,forbidden
from sqlalchemy.orm import Session
from ..utils.hash import verify,hash
from ..models.basemodel import User
from ..utils.ouath2 import create_access_token

def create_user(user: User, db: Session):
    db_user = User(username=user.username, email=user.email, password=user.password)
    
    db_user.password = hash(db_user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(email: str, password: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    
    if not user:
        raise notfound.NotFoundError("User not found")
    
    is_correct = verify(password, user.password)
    
    if not is_correct:
        raise notauthorized.NotAuthorized("Invalid Credentials")
    
    #create access token
    
    access_token = create_access_token(data={"user_email": user.email, "user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
   