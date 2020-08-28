from aa_project.settings import prod


class TestAllowedHostsConfigured:
    def test_allowed_hosts_have_required_hosts(self):
        assert 'wl-portfolio.herokuapp.com' in prod.ALLOWED_HOSTS
        assert 'waynelambert.dev' in prod.ALLOWED_HOSTS
        assert 'www.waynelambert.dev' in prod.ALLOWED_HOSTS


class TestPreDeploymentChecklistCompleted:
    def test_checklist_completed(self):
        assert prod.SECURE_CONTENT_TYPE_NOSNIFF
        assert prod.SECURE_BROWSER_XSS_FILTER
        assert prod.SECURE_SSL_REDIRECT
        assert prod.SESSION_COOKIE_SECURE
        assert prod.CSRF_COOKIE_SECURE
        assert prod.X_FRAME_OPTIONS == 'DENY'
        assert prod.SECURE_HSTS_SECONDS == 2592000
        assert prod.SECURE_HSTS_INCLUDE_SUBDOMAINS
        assert prod.SECURE_HSTS_PRELOAD
        assert prod.SECURE_PROXY_SSL_HEADER == ('HTTP_X_FORWARDED_PROTO', 'https')
        assert prod.SECURE_REFERRER_POLICY == 'same-origin'
