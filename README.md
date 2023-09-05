# fakejwt

Test your web apps against customized [jwts](https://jwt.io/).

Stores fabricated JWT payloads and returning them as encoded JWTs.
Should be useful for testing applications without using real accounts.

Currently opinionated for usage within Språkbanken Text, as a mock for the `/auth/jwt` route of the SB-Auth system.

## Testing

The application under test must be configured to fetch the user's JWT from the fakejwt API.
If the application also verifies the token, it must be configured to use the fake pubkey in [`./conf/pubkey.pem`](./conf/pubkey.pem).

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

Test:

```sh
pytest
```
