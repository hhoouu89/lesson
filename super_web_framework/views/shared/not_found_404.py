from patterns.structural_patterns import *


class NotFound404:
    @Debug(name='NotFound404')
    def __call__(self, request):
        return '404 error', '404 Page Not Found'
