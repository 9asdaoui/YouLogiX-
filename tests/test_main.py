from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "online", "project": "YouLogiX API"}

def test_create_zone():
    payload = {
        "nom": "Test City",
        "codePostal": "12345"
    }
    response = client.post("/zones/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["nom"] == "Test City"
    assert "id" in data

def test_update_colis_status():
    colis_id = 1
    payload = {"nouveauStatut": "en transit"}
    
    response = client.patch(f"/colis/{colis_id}/status", json=payload)
    
    if response.status_code == 200:
        assert response.json()["statut"] == "en transit"
    else:
        assert response.status_code == 404