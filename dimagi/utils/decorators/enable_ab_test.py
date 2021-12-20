from __future__ import absolute_import, print_function
from functools import wraps

from dimagi.utils.ab_tests import AbTest


def enable_ab_test(ab_test_config):
    """Activates A/B test for the current view"""
    def _wrapper(view_func):
        @wraps(view_func)
        def _final_view(request, *args, **kwargs):
            if not hasattr(request, 'ab_test_meta'):
                request.ab_test_meta = []
            if not hasattr(request, 'ab_test'):
                request.ab_test = {}

            # ab_test = AbTest(ab_test_config, request)

            # request.ab_test_meta.append(ab_test.context)
            # request.ab_test[ab_test_config.slug] = ab_test.version()

            response = view_func(request, *args, **kwargs)
            # ab_test.update_response(response)
            return response
        return _final_view
    return _wrapper
