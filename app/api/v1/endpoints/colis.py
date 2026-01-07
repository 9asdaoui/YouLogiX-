from fastapi import APIRouter, Depends, HTTPException
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

@router.patch("/{colis_id}/assign", response_model=schema_colis.Colis)
def assign_driver_to_colis(
    colis_id: int, 
    payload: schema_colis.ColisAssignLivreur, 
    db: Session = Depends(get_db)
):
    updated_colis = crud_colis.assign_livreur(db, colis_id=colis_id, livreur_id=payload.idLivreur)
    
    if not updated_colis:
        raise HTTPException(status_code=404, detail="Colis not found")
        
    return updated_colis

@router.patch("/{colis_id}/status", response_model=schema_colis.Colis)
def update_status(
    colis_id: int, 
    payload: schema_colis.ColisStatusUpdate, 
    db: Session = Depends(get_db)
):
    updated_colis = crud_colis.update_colis_status(db, colis_id=colis_id, status_data=payload)
    
    if not updated_colis:
        raise HTTPException(status_code=404, detail="Colis not found")
        
    return updated_colis