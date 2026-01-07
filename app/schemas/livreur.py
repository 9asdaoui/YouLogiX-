from pydantic import BaseModel

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
    class Config:
        from_attributes = True