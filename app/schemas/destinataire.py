from pydantic import BaseModel

class DestinataireBase(BaseModel):
    nom: str
    prenom: str
    email: str | None = None
    telephone: str
    adresse: str

class DestinataireCreate(DestinataireBase):
    pass

class Destinataire(DestinataireBase):
    id: int
    class Config:
        from_attributes = True
        