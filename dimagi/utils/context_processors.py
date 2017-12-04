from dimagi.utils.config import setting


STATIC_CDN = setting('STATIC_CDN', '')


def global_vars(request):
    return {
        'STATIC_CDN': STATIC_CDN,
    }
