from sqlalchemy.orm import Session
from app.models.colis import Colis
from app.schemas.colis import ColisCreate

def get_colis(db: Session):
    return db.query(Colis).all()

def create_colis(db: Session, colis: ColisCreate):
    db_colis = Colis(**colis.model_dump())
    db.add(db_colis)
    db.commit()
    db.refresh(db_colis)
    return db_colis