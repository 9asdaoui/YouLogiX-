from sqlalchemy.orm import Session
from app.models.colis import Colis
from app.schemas.colis import ColisCreate
from app.models.historique_statut import HistoriqueStatut
from app.schemas.colis import ColisStatusUpdate

def get_colis(db: Session):
    return db.query(Colis).all()

def create_colis(db: Session, colis: ColisCreate):
    db_colis = Colis(**colis.model_dump())
    db.add(db_colis)
    db.commit()
    db.refresh(db_colis)
    return db_colis

def assign_livreur(db: Session, colis_id: int, livreur_id: int):
    db_colis = db.query(Colis).filter(Colis.id == colis_id).first()
    
    if db_colis:
        db_colis.idLivreur = livreur_id
        db.commit()
        db.refresh(db_colis)
    return db_colis

def update_colis_status(db: Session, colis_id: int, status_data: ColisStatusUpdate):

    db_colis = db.query(Colis).filter(Colis.id == colis_id).first()
    
    if not db_colis:
        return None

    ancien_statut = db_colis.statut
    
    db_colis.statut = status_data.nouveauStatut
    
    db_history = HistoriqueStatut(
        idColis=colis_id,
        ancienStatut=ancien_statut,
        nouveauStatut=status_data.nouveauStatut,
        idLivreur=db_colis.idLivreur
    )
    
    db.add(db_history)
    db.commit()
    db.refresh(db_colis)
    
    return db_colis