from pydantic import BaseModel, ConfigDict

class LivreurBase(BaseModel):
    nom: str
    prenom: str
    telephone: str
    vehicule: str | None = None
    zoneAssignee: str | None = None

class LivreurCreate(LivreurBase):
    pass

class Livreur(LivreurBase):
    id: int
    model_config = ConfigDict(from_attributes=True)