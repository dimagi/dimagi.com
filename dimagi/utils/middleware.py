def no_index_middleware(get_response):
    def _middleware(request):
        response = get_response(request)
        response['X-Robots-Tag'] = 'noindex'
        return response
    return _middleware
