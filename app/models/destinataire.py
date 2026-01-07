from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Destinataire(Base):
    __tablename__ = "destinataires"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    email = Column(String, index=True) # Optional unique if needed
    telephone = Column(String, nullable=False)
    adresse = Column(String, nullable=False)