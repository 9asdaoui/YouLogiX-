from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Colis(Base):
    __tablename__ = "colis"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    poids = Column(Float, nullable=False)
    # Statut values: créé, collecté, en stock, en transit, livré
    statut = Column(String, default="créé")
    villeDestination = Column(String, nullable=False)

    # Foreign Keys (The Links)
    # These point to the table name and the ID column
    idClientExpediteur = Column(Integer, ForeignKey("clients_expediteurs.id"), nullable=False)
    idDestinataire = Column(Integer, ForeignKey("destinataires.id"), nullable=False)
    idZone = Column(Integer, ForeignKey("zones.id"), nullable=False)
    
    # idLivreur is nullable=True because a package might not be assigned yet
    idLivreur = Column(Integer, ForeignKey("livreurs.id"), nullable=True)