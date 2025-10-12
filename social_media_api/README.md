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

---

## Posts and Comments Feature

### what you can do now
- create posts with title and content
- edit and delete your own posts
- comment on any post
- edit and delete your own comments
- search posts by title or content
- posts are paginated (10 per page)

### new endpoints

**Posts:**
- `GET /api/posts/` - list all posts
- `POST /api/posts/` - create post (need token)
- `GET /api/posts/{id}/` - get one post
- `PUT /api/posts/{id}/` - update post (must be author)
- `DELETE /api/posts/{id}/` - delete post (must be author)

**Comments:**
- `GET /api/comments/` - list all comments
- `POST /api/comments/` - create comment (need token)
- `GET /api/comments/{id}/` - get one comment
- `PUT /api/comments/{id}/` - update comment (must be author)
- `DELETE /api/comments/{id}/` - delete comment (must be author)

### quick test

1. register and login (get token)

2. create a post:
```bash
curl -X POST http://localhost:8000/api/posts/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"my first post","content":"hello world"}'
```

3. see all posts:
```bash
curl http://localhost:8000/api/posts/
```

4. search posts:
```bash
curl http://localhost:8000/api/posts/?search=first
```

5. add comment:
```bash
curl -X POST http://localhost:8000/api/comments/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"post":1,"content":"great post!"}'
```

### permissions
- anyone can read posts/comments
- need login to create
- only authors can edit/delete their stuff

see POSTS_API_DOCUMENTATION.md for full details!

thats all!
