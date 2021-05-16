from super_web_framework.templator import render
from patterns.structural_patterns import *
from super_web_framework.views.shared.shared import *


@AppRoute(routes=routes, url='/contact/')
class Contact:
    @Debug(name='Contact')
    def __call__(self, request):
        return '200 OK', render('contact.html', data=request.get('data', None))
