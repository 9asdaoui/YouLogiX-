from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.crud import livreur as crud_livreur
from app.schemas import livreur as schema_livreur

router = APIRouter()

@router.get("/", response_model=List[schema_livreur.Livreur])
def read_livreurs(db: Session = Depends(get_db)):
    return crud_livreur.get_livreurs(db)

@router.post("/", response_model=schema_livreur.Livreur)
def create_new_livreur(livreur: schema_livreur.LivreurCreate, db: Session = Depends(get_db)):
    return crud_livreur.create_livreur(db=db, livreur=livreur)