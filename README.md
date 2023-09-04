# fakejwt

Test your web apps against customized [jwts](https://jwt.io/).

## API

| Route          | Method | Request      | Response                                         |
| -------------- | ------ | ------------ | ------------------------------------------------ |
| `/jwt`         | `PUT`  | Payload JSON | The id (int) of stored payload                   |
| `/jwt?id=<id>` | `GET`  |              | The encoded JWT containing the indicated payload |

## Development

Setup:

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run:

```sh
uvicorn app.main:app --reload
# Open your browser at http://127.0.0.1:8000/
```
