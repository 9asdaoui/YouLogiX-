from pydantic import BaseModel
from typing import Optional

class ColisBase(BaseModel):
    description: str
    poids: float
    villeDestination: str
    idClientExpediteur: int
    idDestinataire: int
    idZone: int

class ColisCreate(ColisBase):
    pass

class Colis(ColisBase):
    id: int
    statut: str
    idLivreur: Optional[int] = None # Might be empty at the start

    class Config:
        from_attributes = True