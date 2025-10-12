# Follow System and Feed API Documentation

## Overview
users can follow/unfollow other users and see posts from people they follow in their feed.

## Base URL
```
http://localhost:8000/api/
```

## Authentication
all follow endpoints need token authentication.
```
Authorization: Token your_token_here
```

---

## Follow Endpoints

### 1. Follow a User
**POST** `/api/follow/<user_id>/`

**Authentication:** Required

**Description:** follow another user by their ID

**Example Request:**
```bash
curl -X POST http://localhost:8000/api/follow/2/ \
  -H "Authorization: Token your_token"
```

**Example Response:**
```json
{
  "message": "you are now following john"
}
```

**Errors:**
- cant follow yourself:
```json
{
  "error": "you cant follow yourself"
}
```

- user not found:
```json
{
  "detail": "Not found."
}
```

### 2. Unfollow a User
**POST** `/api/unfollow/<user_id>/`

**Authentication:** Required

**Description:** unfollow a user you are currently following

**Example Request:**
```bash
curl -X POST http://localhost:8000/api/unfollow/2/ \
  -H "Authorization: Token your_token"
```

**Example Response:**
```json
{
  "message": "you unfollowed john"
}
```

---

## Feed Endpoint

### Get Your Feed
**GET** `/api/feed/`

**Authentication:** Required

**Description:** see posts from users you follow, newest first (paginated)

**Query Parameters:**
- `page` - page number (default: 1)

**Example Request:**
```bash
curl http://localhost:8000/api/feed/ \
  -H "Authorization: Token your_token"
```

**Example Response:**
```json
{
  "count": 15,
  "next": "http://localhost:8000/api/feed/?page=2",
  "previous": null,
  "results": [
    {
      "id": 5,
      "author": "john",
      "author_id": 2,
      "title": "Johns Post",
      "content": "this is from someone i follow",
      "created_at": "2025-10-12T14:30:00Z",
      "updated_at": "2025-10-12T14:30:00Z"
    },
    {
      "id": 3,
      "author": "jane",
      "author_id": 3,
      "title": "Janes Update",
      "content": "another post from someone i follow",
      "created_at": "2025-10-12T13:15:00Z",
      "updated_at": "2025-10-12T13:15:00Z"
    }
  ]
}
```

**Notes:**
- only shows posts from users you follow
- if you dont follow anyone, feed will be empty
- posts are ordered by newest first
- 10 posts per page

---

## Complete Workflow Example

### 1. Register two users
```bash
# Register user 1
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","email":"alice@test.com","password":"pass123"}'

# Register user 2
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"bob","email":"bob@test.com","password":"pass123"}'
```

### 2. Login as alice and get token
```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","password":"pass123"}'
```
Save alices token!

### 3. Bob creates a post (login as bob first)
```bash
curl -X POST http://localhost:8000/api/posts/ \
  -H "Authorization: Token bobs_token" \
  -H "Content-Type: application/json" \
  -d '{"title":"Bobs Post","content":"hello from bob"}'
```

### 4. Alice checks her feed (empty because not following anyone)
```bash
curl http://localhost:8000/api/feed/ \
  -H "Authorization: Token alices_token"
```
Result: empty list

### 5. Alice follows Bob
```bash
curl -X POST http://localhost:8000/api/follow/2/ \
  -H "Authorization: Token alices_token"
```
(assuming bob is user id 2)

### 6. Alice checks feed again
```bash
curl http://localhost:8000/api/feed/ \
  -H "Authorization: Token alices_token"
```
Result: sees bobs post!

### 7. Alice unfollows Bob
```bash
curl -X POST http://localhost:8000/api/unfollow/2/ \
  -H "Authorization: Token alices_token"
```

---

## User Model Changes

the CustomUser model now has:
- `followers` - many to many field of users who follow this user
- `following` - reverse relation to see who this user follows

example:
```python
# get users that alice follows
alice.following.all()

# get users who follow alice
alice.followers.all()
```

---

## Permissions

- **Follow/Unfollow:** must be authenticated
- **Feed:** must be authenticated
- **cant follow yourself:** prevented
- **following is not mutual:** if A follows B, doesnt mean B follows A

---

## Tips

- follow multiple users to have a more interesting feed
- feed updates in real time (new posts from followed users appear)
- pagination helps when following many active users
- unfollow removes past posts from feed
