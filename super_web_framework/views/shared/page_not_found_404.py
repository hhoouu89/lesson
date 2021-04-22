class PageNotFound404:
    def __call__(self, request):
        return '404 error', '404 Page Not Found'
