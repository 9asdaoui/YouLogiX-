from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.controllers import colis as colis_controller
from app.schemas import colis as schema_colis

router = APIRouter()

@router.get("/", response_model=List[schema_colis.Colis])
def get_all_colis(
    db: Session = Depends(get_db),
    idZone: int = None,
    statut: str = None
):
    return colis_controller.list_colis(db, id_zone=idZone, statut=statut)

@router.get("/client/{client_id}", response_model=List[schema_colis.Colis])
def get_client_packages(client_id: int, db: Session = Depends(get_db)):
    packages = colis_controller.find_colis_by_client(db, client_id=client_id)
    return packages

@router.get("/{colis_id}", response_model=schema_colis.Colis)
def get_single_colis(colis_id: int, db: Session = Depends(get_db)):
    package = colis_controller.find_colis_by_id(db, colis_id=colis_id)
    if not package:
        raise HTTPException(status_code=404, detail="Package not found")
    return package

@router.get("/livreur/{livreur_id}", response_model=List[schema_colis.Colis])
def get_livreur_packages(livreur_id: int, db: Session = Depends(get_db)):
    return colis_controller.find_colis_by_livreur(db, livreur_id=livreur_id)

@router.post("/", response_model=schema_colis.Colis)
def create_new_colis(colis: schema_colis.ColisCreate, db: Session = Depends(get_db)):
    return colis_controller.store_colis(db=db, colis=colis)

@router.patch("/{colis_id}/assign", response_model=schema_colis.Colis)
def assign_driver_to_colis(
    colis_id: int, 
    payload: schema_colis.ColisAssignLivreur, 
    db: Session = Depends(get_db)
):
    updated_colis = colis_controller.assign_livreur(db, colis_id=colis_id, livreur_id=payload.idLivreur)
    
    if not updated_colis:
        raise HTTPException(status_code=404, detail="Colis not found")
        
    return updated_colis

@router.patch("/{colis_id}/status", response_model=schema_colis.Colis)
def update_status(
    colis_id: int, 
    payload: schema_colis.ColisStatusUpdate, 
    db: Session = Depends(get_db)
):
    updated_colis = colis_controller.update_colis_status(db, colis_id=colis_id, status_data=payload)
    
    if not updated_colis:
        raise HTTPException(status_code=404, detail="Colis not found")
        
    return updated_colis