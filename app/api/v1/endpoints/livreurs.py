from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.controllers import livreur as livreur_controller
from app.schemas import livreur as schema_livreur

router = APIRouter()

@router.get("/", response_model=List[schema_livreur.Livreur])
def get_all_livreurs(db: Session = Depends(get_db)):
    return livreur_controller.list_livreurs(db)

@router.post("/", response_model=schema_livreur.Livreur)
def create_new_livreur(livreur: schema_livreur.LivreurCreate, db: Session = Depends(get_db)):
    return livreur_controller.store_livreur(db=db, livreur=livreur)