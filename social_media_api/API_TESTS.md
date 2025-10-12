# test file for api

## test 1 - register
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@email.com","password":"testpass123"}'
```

## test 2 - login
```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'
```

## postman tests
just copy the json parts and paste in postman body

register json:
```json
{
    "username": "testuser",
    "email": "test@email.com",
    "password": "testpass123"
}
```

login json:
```json
{
    "username": "testuser",
    "password": "testpass123"
}
```
