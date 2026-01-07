from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.controllers import client as client_controller
from app.schemas import client_expediteur as schema_client

router = APIRouter()

@router.get("/", response_model=List[schema_client.Client])
def get_all_clients(db: Session = Depends(get_db)):
    return client_controller.list_clients(db)

@router.post("/", response_model=schema_client.Client)
def create_new_client(client: schema_client.ClientCreate, db: Session = Depends(get_db)):
    return client_controller.store_client(db=db, client=client)