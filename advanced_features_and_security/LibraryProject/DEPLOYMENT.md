# HTTPS Setup

I added these to settings.py:

```python
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
```

For deployment you need SSL certificate and configure web server.

### Nginx example
```
server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /path/to/certificate.crt;
    ssl_certificate_key /path/to/private.key;

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

### Apache example
```
<VirtualHost *:443>
    ServerName yourdomain.com
    SSLEngine on
    SSLCertificateFile /path/to/certificate.crt
    SSLCertificateKeyFile /path/to/private.key
</VirtualHost>
```

## What these settings do

- SECURE_SSL_REDIRECT: Forces HTTPS
- SECURE_HSTS_SECONDS: Tells browsers to use HTTPS for 1 year
- CSRF_COOKIE_SECURE: Only send cookies over HTTPS
- SESSION_COOKIE_SECURE: Only send session cookies over HTTPS