from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_put_get():
    jwt = {
        "sub": "xmatar",
        "name": "Arild",
        "iat": 123,
    }
    response = client.put('/jwt', json=jwt)
    assert response.status_code == 201
    assert response.json() == {"id": 0}

    response = client.get('/jwt', params={"id": 0})
    assert response.status_code == 200
    assert response.json() == jwt
