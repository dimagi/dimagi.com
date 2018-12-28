from dimagi.utils.config import setting
from dimagi.utils.web import get_static_url


def metas(request):
    """
    Used for outputting as JSON to the <meta name="dimagi:*"> tags.
    """
    _metas = {}

    _metas["baseUrl"] = get_static_url('')
    _metas["tracking"] = setting('ANALYTICS')
    _metas["auditABClicks"] = setting('AUDIT_AB_CLICKS')
    _metas["analyticsConfig"] = {
        'logLevel': setting('ANALYTICS_LOG_LEVEL', ''),
        'enabled': setting('ANALYTICS_ENABLED', False),
    }

    return {
        "meta": _metas,
    }


def external_urls(request):
    """
    Used for outputting as JSON to the <meta name="dimagi:*"> tags.
    """
    return {
        "URL_LOGIN": "https://www.commcarehq.org/accounts/login/",
        "URL_TRIAL": "https://www.commcarehq.org/register/user/",
    }


def ab_tests(request):
    if not hasattr(request, 'ab_test_meta'):
        request.ab_test_meta = []
    if not hasattr(request, 'ab_test'):
        request.ab_test = {}
    return {}
