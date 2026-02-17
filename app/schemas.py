from pydantic import BaseModel

class UserCreate(BaseModel):
    email:str
    password:str

class UserLogin(BaseModel):
    email:str
    password:str

class NoteCreate(BaseModel):
    title: str
    description: str

class NoteResponse(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        from_attributes = True
