from __future__ import absolute_import, print_function
from functools import wraps


def enable_amp(view_func):
    """Enables view to access AMP (Accelerated Mobile Pages) features if
    accessed from a mobile or tablet device."""
    @wraps(view_func)
    def _final_view(request, *args, **kwargs):
        request.is_amp = (request.user_agent.is_mobile
                          or request.user_agent.is_tablet)
        return view_func(request, *args, **kwargs)
    return _final_view
