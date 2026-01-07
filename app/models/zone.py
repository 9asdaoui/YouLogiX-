from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Zone(Base):
    __tablename__ = "zones"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    codePostal = Column(String, nullable=False)