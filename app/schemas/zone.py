from pydantic import BaseModel

class ZoneCreate(BaseModel):
    nom: str
    codePostal: str

class Zone(BaseModel):
    id: int
    nom: str
    codePostal: str

    class Config:
        from_attributes = True 