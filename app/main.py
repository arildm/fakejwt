from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from jwt import encode

app = FastAPI()
store = dict()
# This "private" key is not actually secret in this particular app.
with open('conf/privkey.pem', 'rb') as f:
    privkey = f.read()

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex='.*',
    allow_credentials=True,
)

@app.get("/")
def read_root():
    return {"message": "Fakejwt: Test your web apps against customized jwts! See https://github.com/spraakbanken/fakejwt"}


@app.get("/jwt")
def get_jwt(id: int) -> PlainTextResponse:
    if id not in store:
        raise HTTPException(404)
    payload = store[id]
    token = encode(payload, privkey, algorithm="RS256")
    return PlainTextResponse(token)


@app.put("/jwt", status_code=201)
def put_jwt(jwt: dict):
    id = len(store)
    store[id] = jwt
    return {"id": id}