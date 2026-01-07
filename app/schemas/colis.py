from pydantic import BaseModel, ConfigDict
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

    model_config = ConfigDict(from_attributes=True)

class ColisAssignLivreur(BaseModel):
    idLivreur: int

class ColisStatusUpdate(BaseModel):
    nouveauStatut: str # e.g., "collecté", "en transit", "livré"&&&&&&&&&&&&&&