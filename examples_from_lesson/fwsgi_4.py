from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server


# page controller
def index_view(request):
    print(request)
    # возвращаем тело ответа в виде списка из bite
    return '200 OK', [b'Index']


def abc_view(request):
    return '200 OK', [b'ABC']


def not_found_404_view(request):
    print(request)
    return '404 WHAT', [b'404 PAGE Not Found']


routes = {
    '/': index_view,
    '/abc/': abc_view,
}


def application(environ, start_response):
    setup_testing_defaults(environ)
    print(type(environ))
    print(environ)
    path = environ['PATH_INFO']
    if path == '/':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'Index']
    elif path == '/abc/':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return [b'ABC']
    else:
        start_response('404 Not Found', [('Content-Type', 'text/html')])
        return [b'404 Not Found']


with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
