from super_web_framework.templator import render
from patterns.structural_patterns import *
from super_web_framework.views.shared.shared import *


@AppRoute(routes=routes, url='/about/')
class About:
    @Debug(name='About')
    def __call__(self, request):
        return '200 OK', render('about.html', data=request.get('data', None))
