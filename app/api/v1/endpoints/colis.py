from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.crud import colis as crud_colis
from app.schemas import colis as schema_colis

router = APIRouter()

@router.get("/", response_model=List[schema_colis.Colis])
def read_all_colis(db: Session = Depends(get_db)):
    return crud_colis.get_colis(db)

@router.post("/", response_model=schema_colis.Colis)
def create_new_colis(colis: schema_colis.ColisCreate, db: Session = Depends(get_db)):
    return crud_colis.create_colis(db=db, colis=colis)