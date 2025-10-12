# Follow and Feed Testing Guide

## Manual Testing Steps

### Setup: Create Two Test Users

1. **Register user 1 (alice):**
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","email":"alice@test.com","password":"testpass123"}'
```
Save alice's token!

2. **Register user 2 (bob):**
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"bob","email":"bob@test.com","password":"testpass123"}'
```
Save bob's token and user_id!

---

## Test Follow Functionality

### Test 1: Follow a User
```bash
# Alice follows Bob (use bob's user_id from registration)
curl -X POST http://localhost:8000/api/follow/2/ \
  -H "Authorization: Token ALICE_TOKEN"
```

**Expected Response:**
```json
{
  "message": "you are now following bob"
}
```

### Test 2: Try to Follow Yourself (should fail)
```bash
# Alice tries to follow herself
curl -X POST http://localhost:8000/api/follow/1/ \
  -H "Authorization: Token ALICE_TOKEN"
```

**Expected Response:**
```json
{
  "error": "you cant follow yourself"
}
```

### Test 3: Unfollow a User
```bash
# Alice unfollows Bob
curl -X POST http://localhost:8000/api/unfollow/2/ \
  -H "Authorization: Token ALICE_TOKEN"
```

**Expected Response:**
```json
{
  "message": "you unfollowed bob"
}
```

---

## Test Feed Functionality

### Test 4: Empty Feed (not following anyone)
```bash
# Check alice's feed when not following anyone
curl http://localhost:8000/api/feed/ \
  -H "Authorization: Token ALICE_TOKEN"
```

**Expected Response:**
```json
{
  "count": 0,
  "next": null,
  "previous": null,
  "results": []
}
```

### Test 5: Feed with Posts

**Step 1:** Bob creates a post
```bash
curl -X POST http://localhost:8000/api/posts/ \
  -H "Authorization: Token BOB_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Bobs First Post","content":"hello from bob"}'
```

**Step 2:** Alice follows Bob
```bash
curl -X POST http://localhost:8000/api/follow/2/ \
  -H "Authorization: Token ALICE_TOKEN"
```

**Step 3:** Alice checks her feed
```bash
curl http://localhost:8000/api/feed/ \
  -H "Authorization: Token ALICE_TOKEN"
```

**Expected Response:**
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "author": "bob",
      "author_id": 2,
      "title": "Bobs First Post",
      "content": "hello from bob",
      "created_at": "2025-10-12T...",
      "updated_at": "2025-10-12T..."
    }
  ]
}
```

### Test 6: Feed with Multiple Posts

**Step 1:** Bob creates more posts
```bash
curl -X POST http://localhost:8000/api/posts/ \
  -H "Authorization: Token BOB_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Second Post","content":"another post"}'

curl -X POST http://localhost:8000/api/posts/ \
  -H "Authorization: Token BOB_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Third Post","content":"yet another post"}'
```

**Step 2:** Alice checks feed (should see all 3 posts, newest first)
```bash
curl http://localhost:8000/api/feed/ \
  -H "Authorization: Token ALICE_TOKEN"
```

### Test 7: Feed Only Shows Followed Users

**Step 1:** Create user 3 (charlie)
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"charlie","email":"charlie@test.com","password":"testpass123"}'
```

**Step 2:** Charlie creates a post
```bash
curl -X POST http://localhost:8000/api/posts/ \
  -H "Authorization: Token CHARLIE_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Charlies Post","content":"hello from charlie"}'
```

**Step 3:** Alice checks feed (should NOT see charlie's post)
```bash
curl http://localhost:8000/api/feed/ \
  -H "Authorization: Token ALICE_TOKEN"
```
Should only see Bob's posts!

**Step 4:** Alice follows Charlie
```bash
curl -X POST http://localhost:8000/api/follow/3/ \
  -H "Authorization: Token ALICE_TOKEN"
```

**Step 5:** Alice checks feed again (should now see charlie's post too)
```bash
curl http://localhost:8000/api/feed/ \
  -H "Authorization: Token ALICE_TOKEN"
```

### Test 8: Feed Pagination

If there are more than 10 posts from followed users:
```bash
# Get page 1
curl http://localhost:8000/api/feed/?page=1 \
  -H "Authorization: Token ALICE_TOKEN"

# Get page 2
curl http://localhost:8000/api/feed/?page=2 \
  -H "Authorization: Token ALICE_TOKEN"
```

---

## Testing Checklist

- [x] User can follow another user
- [x] User cannot follow themselves
- [x] User can unfollow another user
- [x] Feed is empty when not following anyone
- [x] Feed shows posts from followed users
- [x] Feed does not show posts from unfollowed users
- [x] Feed shows newest posts first
- [x] Feed pagination works (10 posts per page)
- [x] Follow/unfollow requires authentication
- [x] Feed requires authentication
- [x] Following is one-way (not mutual)

---

## Common Issues & Solutions

**Issue:** "Authentication credentials were not provided"
**Solution:** Make sure to include the Authorization header with your token

**Issue:** "Not found"
**Solution:** Check that the user_id exists in the database

**Issue:** Empty feed after following someone
**Solution:** Make sure the followed user has created posts

**Issue:** Seeing posts from users you don't follow
**Solution:** Check that you're using the correct token and the feed endpoint

---

## Test Results Summary

✅ All follow/unfollow operations working
✅ Feed correctly filters posts by followed users
✅ Feed ordered by newest posts first
✅ Pagination working correctly
✅ Permissions enforced
✅ Self-follow prevention working
✅ Authentication required for all endpoints
