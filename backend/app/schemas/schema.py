from pydantic import BaseModel

class UserOut(BaseModel):
    username:str
    phone_number:str
    
class UserCreate(UserOut):
    hashed_password:str


    
    


