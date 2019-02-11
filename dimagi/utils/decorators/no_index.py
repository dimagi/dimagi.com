from __future__ import absolute_import, print_function
from functools import wraps

from dimagi.utils.config import setting


def no_index(view_func):
    """Decorator to prevent a page from being indexable by robots"""
    @wraps(view_func)
    def _added_header(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)
        response['X-Robots-Tag'] = 'noindex'
        return response
    return _added_header
