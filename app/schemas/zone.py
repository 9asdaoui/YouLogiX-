from pydantic import BaseModel, ConfigDict

class ZoneCreate(BaseModel):
    nom: str
    codePostal: str

class Zone(BaseModel):
    id: int
    nom: str
    codePostal: str

    model_config = ConfigDict(from_attributes=True)
