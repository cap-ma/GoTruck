from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from dbs.database import SessionLocal
from schemas.schema import UserOut,UserCreate
from logics.logic import create_user

user_route=APIRouter()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



@user_route.post("user_register",response_model=UserOut)
async def register_user(user:UserCreate,db:Session=Depends(get_db)):
    db_user=await create_user(db=db,user=user)
    return db_user