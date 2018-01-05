from dimagi.utils.web import get_static_url


def metas(request):
    """
    Used for outputting as JSON to the <meta name="dimagi:*"> tags.
    """
    _metas = {}
    _metas["baseUrl"] = get_static_url('')
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
