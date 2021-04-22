from super_web_framework.super_web_framework import SuperWebFramework
from urls import routes, fronts


def application(environment, start_response):
    return SuperWebFramework(routes, fronts)
