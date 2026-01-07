from sqlalchemy.orm import Session
from app.models.destinataire import Destinataire
from app.schemas.destinataire import DestinataireCreate

def get_destinataires(db: Session):
    return db.query(Destinataire).all()

def create_destinataire(db: Session, destinataire: DestinataireCreate):
    db_destinataire = Destinataire(**destinataire.model_dump())
    db.add(db_destinataire)
    db.commit()
    db.refresh(db_destinataire)
    return db_destinataire