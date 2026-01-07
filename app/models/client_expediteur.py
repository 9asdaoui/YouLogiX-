from sqlalchemy import Column, Integer, String
from app.db.base import Base

class ClientExpediteur(Base):
    __tablename__ = "clients_expediteurs"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    telephone = Column(String, nullable=False)
    adresse = Column(String, nullable=False)