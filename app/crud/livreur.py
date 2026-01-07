from sqlalchemy.orm import Session
from app.models.livreur import Livreur
from app.schemas.livreur import LivreurCreate

def get_livreurs(db: Session):
    return db.query(Livreur).all()

def create_livreur(db: Session, livreur: LivreurCreate):
    db_livreur = Livreur(**livreur.model_dump())
    db.add(db_livreur)
    db.commit()
    db.refresh(db_livreur)
    return db_livreur