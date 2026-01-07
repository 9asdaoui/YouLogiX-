from pydantic import BaseModel, EmailStr

class ClientBase(BaseModel):
    nom: str
    prenom: str
    email: str
    telephone: str
    adresse: str

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int
    class Config:
        from_attributes = True