# how to add login to api

i added some login stuff to my book api. now some urls need passwords.

## what i did

1. put `rest_framework.authtoken` in settings
2. added REST_FRAMEWORK thing (dont know what it does)
3. made /api-token-auth/ url
4. put permission_classes on BookViewSet

## how to test it

### make admin user:
```
python manage.py createsuperuser
```

### get token:
```
curl -d "username=admin&password=yourpassword" http://127.0.0.1:8000/api/api-token-auth/
```

returns:
```
{"token":"abc123def456"}
```

### use token:
```
curl -H "Authorization: Token abc123def456" http://127.0.0.1:8000/api/books_all/
```

## what works without login

- /api/books/ still works without token
- only /api/books_all/ needs token now

## what doesnt work without login

trying this without token:
```
curl http://127.0.0.1:8000/api/books_all/
```

gives error:
```
{"detail":"Authentication credentials were not provided."}
```

## my code changes

settings.py:
```python
INSTALLED_APPS = [
    'rest_framework.authtoken',  # idk what this does but need it for auth
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
    # TODO: add more later maybe?
}
```

views.py:
```python
class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # need to login first
```

urls.py:
```python
path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # login thing
```

dont forget:
```
python manage.py migrate
```

still dont understand why this is needed but it works