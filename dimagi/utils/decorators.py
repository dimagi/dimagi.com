from functools import wraps


def no_index(view_func):
    """Decorator to prevent a page from being indexable by robots"""
    @wraps(view_func)
    def _added_header(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)
        response['X-Robots-Tag'] = 'noindex'
        return response
    return _added_header
