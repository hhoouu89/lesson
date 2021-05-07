from datetime import date
from super_web_framework.views.index import Index
from super_web_framework.views.about import About
from super_web_framework.views.contact import Contact


def front_layer_1(request):
    request['data'] = date.today()


def front_layer_2(request):
    request['key'] = 'key'


fronts = [front_layer_1, front_layer_2]

routes = {
    '/': Index(),
    '/index/': Index(),
    '/about/': About(),
    '/contact/': Contact(),
}
