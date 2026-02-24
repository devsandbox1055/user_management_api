from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email:EmailStr

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class config:
        from_attributes =True 
## Agar dict nahi mila, to object ke attributes read karke model bana lo
# this will sucessfully convert ORM object into json response