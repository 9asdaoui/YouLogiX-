from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.crud import client_expediteur as crud_client
from app.schemas import client_expediteur as schema_client

router = APIRouter()

@router.get("/", response_model=List[schema_client.Client])
def read_clients(db: Session = Depends(get_db)):
    return crud_client.get_clients(db)

@router.post("/", response_model=schema_client.Client)
def create_new_client(client: schema_client.ClientCreate, db: Session = Depends(get_db)):
    return crud_client.create_client(db=db, client=client)