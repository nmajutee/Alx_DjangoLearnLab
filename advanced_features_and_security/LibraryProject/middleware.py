"""
Custom middleware to add Content Security Policy headers for enhanced security.
"""

from django.utils.deprecation import MiddlewareMixin


class SecurityHeadersMiddleware(MiddlewareMixin):
    """
    Middleware to add security headers to all responses.
    """

    def process_response(self, request, response):
        # Content Security Policy - prevents XSS attacks
        response['Content-Security-Policy'] = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; "
            "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; "
            "img-src 'self' data:; "
            "font-src 'self' https://cdn.jsdelivr.net; "
            "connect-src 'self'; "
            "frame-ancestors 'none';"
        )

        # Additional security headers
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        response['Permissions-Policy'] = 'geolocation=(), microphone=(), camera=()'

        return response