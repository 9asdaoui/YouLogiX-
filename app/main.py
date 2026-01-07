from fastapi import FastAPI, Depends, HTTPException 
from app.core.config import settings
from app.db.session import get_db
from sqlalchemy.orm import Session
import app.models
from app.db.session import engine
from app.db.base import Base
from app.api.v1.endpoints import zones, livreurs, clients, destinataires, colis


Base.metadata.create_all(bind=engine)

# app = FastAPI(title=settings.PROJECT_NAME)

app = FastAPI(
    title="YouLogiX — Plateforme Logistique",
    description="""
    API de gestion des opérations logistiques pour YouExpress.
    
    ### Utilisateurs:
    * **Gestionnaire**: CRUD complet sur tout le système.
    * **Livreur**: Mise à jour du statut des colis.
    * **Client**: Suivi des envois.
    """,
    version="1.0.0",
    contact={
        "name": "Oussama Qasdaoui",
        "email": "oussamaqasdaoui@gmail.com",
    }
)

@app.get("/")
def read_root():
    return {"status": "online", "project": settings.PROJECT_NAME}

app.include_router(zones.router, prefix="/zones", tags=["Zones"])
app.include_router(clients.router, prefix="/clients", tags=["Clients"])
app.include_router(destinataires.router, prefix="/destinataires", tags=["Destinataires"])
app.include_router(livreurs.router, prefix="/livreurs", tags=["Livreurs"])
app.include_router(colis.router, prefix="/colis", tags=["Colis"])


@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    return {"status": "Database connection is successful"}


@app.get("/test-error")
def test_error():
    raise HTTPException(status_code=404, detail="Item not found!")