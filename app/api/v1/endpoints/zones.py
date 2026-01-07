from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.controllers import zone as zone_controller
from app.schemas import zone as schema_zone

router = APIRouter()

@router.get("/", response_model=List[schema_zone.Zone])
def get_all_zones(db: Session = Depends(get_db)):
    return zone_controller.list_zones(db)

@router.post("/", response_model=schema_zone.Zone)
def create_new_zone(zone: schema_zone.ZoneCreate, db: Session = Depends(get_db)):
    return zone_controller.store_zone(db=db, zone=zone)