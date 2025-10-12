# API Testing Guide

## Quick Test Commands

### 1. Register a user
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@test.com","password":"testpass123"}'
```

### 2. Login to get token
```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'
```

Save the token from response!

### 3. Create a post
```bash
curl -X POST http://localhost:8000/api/posts/ \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"title":"Test Post","content":"This is a test post"}'
```

### 4. List all posts
```bash
curl http://localhost:8000/api/posts/
```

### 5. Search posts
```bash
curl "http://localhost:8000/api/posts/?search=test"
```

### 6. Create a comment
```bash
curl -X POST http://localhost:8000/api/comments/ \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"post":1,"content":"Great post!"}'
```

### 7. List all comments
```bash
curl http://localhost:8000/api/comments/
```

### 8. Update your post
```bash
curl -X PUT http://localhost:8000/api/posts/1/ \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated Title","content":"Updated content"}'
```

### 9. Delete your post
```bash
curl -X DELETE http://localhost:8000/api/posts/1/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

## Testing Results

All endpoints tested and working:
✅ User registration
✅ User login
✅ Create post (authenticated)
✅ List posts (public)
✅ Search posts (public)
✅ Update post (author only)
✅ Delete post (author only)
✅ Create comment (authenticated)
✅ List comments (public)
✅ Update comment (author only)
✅ Delete comment (author only)
✅ Pagination working on posts
✅ Permissions working correctly
