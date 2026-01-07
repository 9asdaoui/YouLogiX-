from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Livreur(Base):
    __tablename__ = "livreurs"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    telephone = Column(String, nullable=False)
    vehicule = Column(String)
    zoneAssignee = Column(String)