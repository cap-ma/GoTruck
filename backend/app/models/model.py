
from app.dbs.database_user import Base
from sqlalchemy import Integer,String,Boolean,Column
import sqlalchemy
class User(Base):
    __tablename__="user_register"
    
    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    username=Column(String,unique=True,index=True)
    hashed_password=Column(String)
    phone_number=Column(String,index=True)

