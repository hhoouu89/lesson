from super_web_framework.super_web_framework import SuperWebFramework
from urls import routes, fronts
from wsgiref.simple_server import make_server

application = SuperWebFramework(routes, fronts)

with make_server('', 8080, application) as httpd:
    print("Запуск... Порт 8080...")
    httpd.serve_forever()
