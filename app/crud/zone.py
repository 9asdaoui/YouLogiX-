from sqlalchemy.orm import Session
from app.models.zone import Zone
from app.schemas.zone import ZoneCreate

def get_zones(db: Session):
    return db.query(Zone).all()

def create_zone(db: Session, zone: ZoneCreate):
    db_zone = Zone(nom=zone.nom, codePostal=zone.codePostal)
    db.add(db_zone)
    db.commit()
    db.refresh(db_zone)
    return db_zone