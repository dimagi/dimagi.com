from dimagi.utils.config import setting
from dimagi.utils.web import get_static_url


def metas(request):
    """
    Used for outputting as JSON to the <meta name="dimagi:*"> tags.
    """
    _metas = {}

    _metas["baseUrl"] = get_static_url('')
    _metas["tracking"] = setting('TRACKING')
    _metas["auditABClicks"] = setting('AUDIT_AB_CLICKS')
    _metas["trackingConfig"] = {
        'logLevel': setting('TRACKING_LOG_LEVEL', ''),
        'enabled': setting('TRACKING_ENABLED', False),
        'optimizeId': setting('GOOGLE_OPTIMIZE_ID', ''),
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
