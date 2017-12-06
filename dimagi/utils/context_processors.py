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
