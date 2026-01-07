from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.controllers import destinataire as destinataire_controller
from app.schemas import destinataires as schema_destinataires

router = APIRouter()

@router.get("/", response_model=List[schema_destinataires.Destinataire])
def get_all_destinataires(db: Session = Depends(get_db)):
    return destinataire_controller.list_destinataires(db)

@router.post("/", response_model=schema_destinataires.Destinataire)
def create_new_destinataire(destinataire: schema_destinataires.DestinataireCreate, db: Session = Depends(get_db)):
    return destinataire_controller.store_destinataire(db=db, destinataire=destinataire)