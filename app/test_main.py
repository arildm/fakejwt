from fastapi.testclient import TestClient
from jwt import decode
from .main import app

client = TestClient(app)

with open('conf/pubkey.pem', 'rb') as f:
    pubkey = f.read()

def test_put_get():
    payload = {
        "sub": "xmatar",
        "name": "Arild",
        "iat": 123,
    }
    response = client.put('/jwt/foo', json=payload)
    assert response.status_code == 201
    assert response.json() == {"id": "foo"}

    response = client.get('/jwt/foo')
    assert response.status_code == 200
    assert decode(response.read(), options={"verify_signature": False}) == payload
    assert decode(response.read(), pubkey, algorithms="RS256")

def test_put_bad():
    response = client.put('/jwt/foo', content="foobar")
    assert response.status_code == 422

def test_get_missing():
    response = client.get('/jwt/bar')
    assert response.status_code == 404

def test_any():
    payload = {
        "sub" : "xmatar",
        "name" : "Arild",
        "iat" : 123,
        "foo": "bar",
    }
    response = client.put('/jwt/foo', json=payload)
    assert response.status_code == 201
    assert response.json() == {"id": "foo"}

    response = client.get('/jwt/foo')
    assert response.status_code == 200
    assert decode(response.read(), pubkey, algorithms="RS256") == payload