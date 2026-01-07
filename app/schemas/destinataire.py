from pydantic import BaseModel, ConfigDict

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
    model_config = ConfigDict(from_attributes=True)
