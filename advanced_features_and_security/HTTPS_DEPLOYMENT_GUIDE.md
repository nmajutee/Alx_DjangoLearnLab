# Django HTTPS Deployment Guide

## Web Server Configuration

### Nginx Configuration (recommended)
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    ssl_certificate /path/to/certificate.crt;
    ssl_certificate_key /path/to/private.key;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;
    ssl_prefer_server_ciphers off;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Apache Configuration
```apache
<VirtualHost *:80>
    ServerName yourdomain.com
    Redirect permanent / https://yourdomain.com/
</VirtualHost>

<VirtualHost *:443>
    ServerName yourdomain.com

    SSLEngine on
    SSLCertificateFile /path/to/certificate.crt
    SSLCertificateKeyFile /path/to/private.key

    ProxyPass / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/
    ProxyPreserveHost On
    ProxyAddHeaders On
</VirtualHost>
```

## SSL Certificate Setup

### Let's Encrypt (Free SSL)
```bash
# Install certbot
sudo apt install certbot python3-certbot-nginx

# Obtain certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Auto-renewal
sudo systemctl enable certbot.timer
```

## Security Headers Verification

Test your HTTPS configuration at:
- https://www.ssllabs.com/ssltest/
- https://securityheaders.com/

## Production Deployment Checklist

- [ ] SSL certificate installed
- [ ] SECURE_SSL_REDIRECT = True
- [ ] SECURE_HSTS_SECONDS = 31536000
- [ ] SECURE_HSTS_INCLUDE_SUBDOMAINS = True
- [ ] SECURE_HSTS_PRELOAD = True
- [ ] SESSION_COOKIE_SECURE = True
- [ ] CSRF_COOKIE_SECURE = True
- [ ] Web server configured for HTTPS
- [ ] HTTP to HTTPS redirects working
- [ ] All static files served over HTTPS