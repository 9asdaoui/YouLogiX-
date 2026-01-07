from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.crud import destinataires as crud_destinataires
from app.schemas import destinataires as schema_destinataires

router = APIRouter()

@router.get("/", response_model=List[schema_destinataires.Destinataire])
def read_destinataires(db: Session = Depends(get_db)):
    return crud_destinataires.get_destinataires(db)

@router.post("/", response_model=schema_destinataires.Destinataire)
def create_new_destinataire(destinataire: schema_destinataires.DestinataireCreate, db: Session = Depends(get_db)):
    return crud_destinataires.create_destinataire(db=db, destinataire=destinataire)