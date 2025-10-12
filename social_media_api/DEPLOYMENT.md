# Deployment Guide - Social Media API on Render

## what this is
this guide shows how to deploy the social media api to render. render is free and easy to use.

## what you need
- github account with your code pushed
- render account (free at render.com)
- this takes about 10-15 minutes

## step 1: prepare your code

all the files are already set up:
- `requirements.txt` - all packages needed
- `build.sh` - script that runs on render
- `render.yaml` - render configuration
- `.env.example` - shows what environment variables you need
- `settings.py` - updated for production

make sure everything is pushed to github:
```bash
git add .
git commit -m "ready for deployment"
git push
```

## step 2: create render account

1. go to https://render.com
2. click "Get Started" 
3. sign up with github (easiest way)
4. authorize render to access your repos

## step 3: create postgresql database

render needs a database for production:

1. click "New +" button
2. select "PostgreSQL"
3. fill in:
   - Name: `social-media-db`
   - Database: `social_media_db`
   - User: `social_media_user`
   - Region: choose closest to you
   - Plan: Free
4. click "Create Database"
5. wait for it to finish (takes 1-2 minutes)
6. save the "Internal Database URL" - you'll need this

## step 4: create web service

now deploy the django app:

1. click "New +" button
2. select "Web Service"
3. connect your github repo:
   - find "Alx_DjangoLearnLab"
   - click "Connect"
4. fill in settings:
   - Name: `social-media-api`
   - Region: same as database
   - Branch: `main`
   - Root Directory: `social_media_api`
   - Runtime: `Python 3`
   - Build Command: `./build.sh`
   - Start Command: `gunicorn social_media_api.wsgi:application`
   - Plan: Free

## step 5: add environment variables

scroll down to "Environment Variables" section:

add these variables:

1. `SECRET_KEY`
   - click "Generate" to create random key
   
2. `DEBUG`
   - Value: `False`
   
3. `DATABASE_URL`
   - paste the Internal Database URL from step 3
   
4. `ALLOWED_HOSTS`
   - Value: `your-app-name.onrender.com`
   - replace "your-app-name" with actual render url
   - example: `social-media-api.onrender.com`

5. `PYTHON_VERSION`
   - Value: `3.8.10`

click "Create Web Service"

## step 6: wait for deployment

render will now:
1. clone your github repo
2. install requirements
3. run build.sh (migrations and collect static files)
4. start gunicorn server

this takes 5-10 minutes for first deployment.

watch the logs to see progress.

## step 7: test your api

once deployed, you'll get a url like:
`https://social-media-api.onrender.com`

test the endpoints:

1. health check:
```bash
curl https://social-media-api.onrender.com/api/
```

2. register user:
```bash
curl -X POST https://social-media-api.onrender.com/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@test.com","password":"testpass123"}'
```

3. login:
```bash
curl -X POST https://social-media-api.onrender.com/api/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'
```

save the token from response!

4. create post:
```bash
curl -X POST https://social-media-api.onrender.com/api/posts/ \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"title":"my first post","content":"hello from render!"}'
```

## important notes

### free tier limitations
- app sleeps after 15 minutes of inactivity
- first request after sleep takes 30-60 seconds
- 750 hours/month free (enough for one app)
- database has 90 day expiration on free tier

### security settings
production security is enabled when DEBUG=False:
- HTTPS redirect
- secure cookies
- XSS protection
- clickjacking protection
- content type sniffing protection

### static files
whitenoise handles static files automatically. no need for separate cdn.

### database backups
free tier doesn't include automatic backups. upgrade to paid plan for backups.

## troubleshooting

### deployment failed
check the logs in render dashboard:
- look for error messages
- common issues: missing packages, wrong python version, database connection errors

### 500 error
1. check environment variables are set correctly
2. make sure ALLOWED_HOSTS includes your render url
3. check database url is correct
4. view logs for error details

### static files not loading
1. make sure whitenoise is in MIDDLEWARE
2. run collectstatic: render runs this automatically via build.sh
3. check STATIC_ROOT and STATIC_URL in settings.py

### database connection error
1. verify DATABASE_URL environment variable
2. make sure database is running (check render dashboard)
3. check database is in same region as web service

## updating your app

when you make changes:

1. commit and push to github:
```bash
git add .
git commit -m "update feature"
git push
```

2. render auto-deploys on push (if enabled)
   - or manually click "Deploy latest commit" in render dashboard

3. deployment takes 2-5 minutes

## monitoring

render provides:
- live logs
- metrics (cpu, memory)
- events history

check these regularly to catch issues.

## next steps

after deployment works:

1. set up custom domain (optional)
2. upgrade to paid plan for:
   - no sleep
   - automatic backups
   - more resources
3. set up error monitoring (sentry)
4. add CI/CD tests before deploy

## production settings reference

key settings in settings.py:

```python
DEBUG = False  # never True in production
ALLOWED_HOSTS = ['your-domain.onrender.com']  # your render url
SECRET_KEY = 'use-environment-variable'  # never hardcode
DATABASE_URL = 'postgres://...'  # postgres for production
```

security settings automatically enabled when DEBUG=False:
- SECURE_BROWSER_XSS_FILTER = True
- X_FRAME_OPTIONS = 'DENY'
- SECURE_CONTENT_TYPE_NOSNIFF = True
- SECURE_SSL_REDIRECT = True
- SESSION_COOKIE_SECURE = True
- CSRF_COOKIE_SECURE = True

## files for deployment

all these files are required:

1. `requirements.txt` - python packages
2. `build.sh` - deployment script
3. `render.yaml` - render configuration (optional but helpful)
4. `.env.example` - environment variable template
5. `settings.py` - production settings
6. `.gitignore` - don't commit sensitive files

## support

render docs: https://render.com/docs
render community: https://community.render.com

## your deployed api

once deployed, your api will be at:
**https://your-app-name.onrender.com**

available endpoints:
- POST /api/register/ - register user
- POST /api/login/ - login user
- GET/POST /api/posts/ - list/create posts
- GET/POST /api/comments/ - list/create comments
- POST /api/follow/<user_id>/ - follow user
- POST /api/unfollow/<user_id>/ - unfollow user
- GET /api/feed/ - personalized feed
- POST /api/posts/<id>/like/ - like post
- POST /api/posts/<id>/unlike/ - unlike post
- GET /api/notifications/ - list notifications
- POST /api/notifications/<id>/read/ - mark as read

all endpoints work the same as local, just change the url!

good luck with deployment!
