from pydantic import BaseModel

class UserOut(BaseModel):
    username:str
    phone_number:str

    class Config:
        orm_mode=True

class UserCreate(UserOut):
    hashed_password:str
    class Config:
        orm_mode=True


    
    


