from pydantic import BaseModel, ConfigDict

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
    model_config = ConfigDict(from_attributes=True)