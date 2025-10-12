# Posts and Comments API Documentation

## Overview
This API allows users to create, read, update and delete posts and comments.

## Base URL
```
http://localhost:8000/api/
```

## Authentication
Most endpoints require authentication using Token Authentication.
Include the token in the header:
```
Authorization: Token your_token_here
```

---

## Posts Endpoints

### 1. List All Posts (with pagination)
**GET** `/api/posts/`

**Description:** Get a list of all posts (10 per page)

**Query Parameters:**
- `page` - Page number (default: 1)
- `search` - Search posts by title or content

**Example Request:**
```bash
curl http://localhost:8000/api/posts/
curl http://localhost:8000/api/posts/?page=2
curl http://localhost:8000/api/posts/?search=django
```

**Example Response:**
```json
{
  "count": 25,
  "next": "http://localhost:8000/api/posts/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "author": "john",
      "author_id": 1,
      "title": "My First Post",
      "content": "This is my first post content",
      "created_at": "2025-10-12T10:30:00Z",
      "updated_at": "2025-10-12T10:30:00Z"
    }
  ]
}
```

### 2. Create New Post
**POST** `/api/posts/`

**Authentication:** Required

**Request Body:**
```json
{
  "title": "My Post Title",
  "content": "Post content here"
}
```

**Example Request:**
```bash
curl -X POST http://localhost:8000/api/posts/ \
  -H "Authorization: Token your_token" \
  -H "Content-Type: application/json" \
  -d '{"title":"New Post","content":"Post content"}'
```

**Example Response:**
```json
{
  "id": 2,
  "author": "john",
  "author_id": 1,
  "title": "New Post",
  "content": "Post content",
  "created_at": "2025-10-12T11:00:00Z",
  "updated_at": "2025-10-12T11:00:00Z"
}
```

### 3. Get Single Post
**GET** `/api/posts/{id}/`

**Example Request:**
```bash
curl http://localhost:8000/api/posts/1/
```

### 4. Update Post
**PUT** `/api/posts/{id}/`

**Authentication:** Required (must be author)

**Request Body:**
```json
{
  "title": "Updated Title",
  "content": "Updated content"
}
```

**Example Request:**
```bash
curl -X PUT http://localhost:8000/api/posts/1/ \
  -H "Authorization: Token your_token" \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated","content":"New content"}'
```

### 5. Partial Update Post
**PATCH** `/api/posts/{id}/`

**Authentication:** Required (must be author)

**Request Body:** (only fields you want to update)
```json
{
  "title": "New Title"
}
```

### 6. Delete Post
**DELETE** `/api/posts/{id}/`

**Authentication:** Required (must be author)

**Example Request:**
```bash
curl -X DELETE http://localhost:8000/api/posts/1/ \
  -H "Authorization: Token your_token"
```

---

## Comments Endpoints

### 1. List All Comments
**GET** `/api/comments/`

**Example Request:**
```bash
curl http://localhost:8000/api/comments/
```

**Example Response:**
```json
[
  {
    "id": 1,
    "post": 1,
    "post_title": "My First Post",
    "author": "jane",
    "author_id": 2,
    "content": "Great post!",
    "created_at": "2025-10-12T10:45:00Z",
    "updated_at": "2025-10-12T10:45:00Z"
  }
]
```

### 2. Create New Comment
**POST** `/api/comments/`

**Authentication:** Required

**Request Body:**
```json
{
  "post": 1,
  "content": "This is my comment"
}
```

**Example Request:**
```bash
curl -X POST http://localhost:8000/api/comments/ \
  -H "Authorization: Token your_token" \
  -H "Content-Type: application/json" \
  -d '{"post":1,"content":"Nice post!"}'
```

### 3. Get Single Comment
**GET** `/api/comments/{id}/`

**Example Request:**
```bash
curl http://localhost:8000/api/comments/1/
```

### 4. Update Comment
**PUT** `/api/comments/{id}/`

**Authentication:** Required (must be author)

**Request Body:**
```json
{
  "post": 1,
  "content": "Updated comment text"
}
```

### 5. Partial Update Comment
**PATCH** `/api/comments/{id}/`

**Authentication:** Required (must be author)

**Request Body:**
```json
{
  "content": "Updated comment"
}
```

### 6. Delete Comment
**DELETE** `/api/comments/{id}/`

**Authentication:** Required (must be author)

**Example Request:**
```bash
curl -X DELETE http://localhost:8000/api/comments/1/ \
  -H "Authorization: Token your_token"
```

---

## Permissions

- **Read (GET):** Anyone can view posts and comments
- **Create (POST):** Must be authenticated
- **Update (PUT/PATCH):** Must be authenticated AND be the author
- **Delete (DELETE):** Must be authenticated AND be the author

## Search & Filtering

Posts support searching by title or content:
```bash
# Search for posts containing "django"
curl http://localhost:8000/api/posts/?search=django

# Search for posts containing "tutorial"
curl http://localhost:8000/api/posts/?search=tutorial
```

## Pagination

Posts are paginated with 10 posts per page:
```bash
# Get page 1
curl http://localhost:8000/api/posts/?page=1

# Get page 2
curl http://localhost:8000/api/posts/?page=2
```

## Error Responses

### 401 Unauthorized
```json
{
  "detail": "Authentication credentials were not provided."
}
```

### 403 Forbidden
```json
{
  "detail": "You do not have permission to perform this action."
}
```

### 404 Not Found
```json
{
  "detail": "Not found."
}
```

### 400 Bad Request
```json
{
  "title": ["This field is required."],
  "content": ["This field may not be blank."]
}
```
