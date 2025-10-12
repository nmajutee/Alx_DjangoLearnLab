# Social Media API

## what this does
this is my simple api for social media. you can register and login users.

## how to run

1. install packages:
```
pip install django djangorestframework pillow
```

2. setup database:
```
python manage.py migrate
```

3. start the server:
```
python manage.py runserver
```

## using the api

### register user
POST to: `http://localhost:8000/api/register/`

send:
```json
{
    "username": "john",
    "email": "john@test.com",
    "password": "pass123"
}
```

you get token back. save it!

example response:
```json
{
    "token": "abc123456token",
    "user_id": 1,
    "username": "john"
}
```

### Login
**POST** to `http://127.0.0.1:8000/api/login/`

### login user
POST to: `http://localhost:8000/api/login/`

send:
```json
{
    "username": "john",
    "password": "pass123"
}
```

same response with token

## user model has
- username
- email
- password (encrypted)
- bio
- profile_picture
- followers

## important files
- `models.py` - user stuff
- `views.py` - login/register code
- `serializers.py` - json converter
- `urls.py` - api routes

## testing
use postman:
1. make POST request
2. url: `http://localhost:8000/api/register/`
3. select raw + JSON
4. paste json data
5. send

save the token!

## notes
- tokens expire never (bad practice but works)
- password must be atleast 8 chars
- bio is optional

thats all!
