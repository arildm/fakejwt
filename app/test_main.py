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

def test_put_bad():
    response = client.put('/jwt', content="foobar")
    assert response.status_code == 422

def test_get_missing():
    response = client.get('/jwt', params={"id": 123})
    assert response.status_code == 404