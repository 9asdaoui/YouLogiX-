from sqlalchemy.orm import Session
from app.models.client_expediteur import ClientExpediteur
from app.schemas.client_expediteur import ClientCreate

def list_clients(db: Session):
    return db.query(ClientExpediteur).all()

def store_client(db: Session, client: ClientCreate):
    db_client = ClientExpediteur(**client.model_dump())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client