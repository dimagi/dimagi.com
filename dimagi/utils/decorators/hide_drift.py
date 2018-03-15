from __future__ import absolute_import, print_function
from functools import wraps


def hide_drift(view_func):
    """Prevents loading of drift"""
    @wraps(view_func)
    def _added_header(request, *args, **kwargs):
        request.hide_drift = True
        return view_func(request, *args, **kwargs)
    return _added_header
