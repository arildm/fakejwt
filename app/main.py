from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Jwt(BaseModel):
    sub: str
    name: str
    iat: int

  
store = dict()


@app.get("/")
def read_root():
    return {"message": "Fakejwt: Test your web apps against customized jwts! See https://github.com/spraakbanken/fakejwt"}


@app.get("/jwt")
def get_jwt(id: int):
    if (id not in store):
        raise HTTPException(404)
    return store[id]


@app.put("/jwt")
def put_jwt(jwt: Jwt):
    id = len(store)
    store[id] = jwt
    return {"id": id}