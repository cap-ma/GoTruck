from sqlalchemy.orm import Session
from models import model
from schemas import schema

def create_user(db:Session,user:schema.UserCreate):
    db_user=model.User(username=user.username,hashed_password=user.hashed_password,phone_number=user.phone_number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user