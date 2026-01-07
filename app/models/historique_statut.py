from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
import datetime
from app.db.base import Base

class HistoriqueStatut(Base):
    __tablename__ = "historique_statuts"

    id = Column(Integer, primary_key=True, index=True)
    idColis = Column(Integer, ForeignKey("colis.id"), nullable=False)
    ancienStatut = Column(String)
    nouveauStatut = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    idLivreur = Column(Integer, ForeignKey("livreurs.id"), nullable=True)