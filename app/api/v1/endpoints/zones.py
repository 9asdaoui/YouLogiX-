from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.crud import zone as crud_zone
from app.schemas import zone as schema_zone

router = APIRouter()

@router.get("/", response_model=List[schema_zone.Zone])
def read_zones(db: Session = Depends(get_db)):
    return crud_zone.get_zones(db)

@router.post("/", response_model=schema_zone.Zone)
def create_new_zone(zone: schema_zone.ZoneCreate, db: Session = Depends(get_db)):
    return crud_zone.create_zone(db=db, zone=zone)