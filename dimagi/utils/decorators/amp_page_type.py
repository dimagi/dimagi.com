from __future__ import absolute_import, print_function
from functools import wraps


class AmpPageType(object):
    PILLAR = 'pillar'
    BASIC = 'basic'


def set_amp_page_type(page_type):
    """Allows you to set a an amp_page_type that can be used by AMP
    (Accelerated Mobile Pages) to hide / show certain features specific to that
    AMP page."""
    def _wrapper(view_func):
        @wraps(view_func)
        def _final_view(request, *args, **kwargs):
            request.amp_page_type = page_type
            return view_func(request, *args, **kwargs)
        return _final_view
    return _wrapper
