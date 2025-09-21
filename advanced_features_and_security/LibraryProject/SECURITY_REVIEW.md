# Security Review

I added HTTPS settings:

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

This makes the site use HTTPS and keeps cookies secure.
2. Protects against man-in-the-middle attacks
3. Keeps cookies secure
4. Browser remembers to use HTTPS

## What could be improved:

1. Use a proper SSL certificate in production
2. Test with real HTTPS setup
3. Monitor for mixed content issues
4. Consider adding Content Security Policy

## Testing:

To test HTTPS:
1. Deploy with SSL certificate
2. Check that HTTP redirects to HTTPS
3. Verify security headers in browser dev tools
4. Test that cookies work correctly