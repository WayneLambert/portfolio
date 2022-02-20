""" Helper functions to facilitate testing """

from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware


def add_middleware_to_request(request, middleware_class):
    """
    Supports a testing scenario which simulates an active middleware
    session within the lifecycle of a request.
    """
    middleware = middleware_class(request)
    middleware.process_request(request)
    request.session.save()
    return request

def add_middlewares(request):
    """ Supports adding session/messages middleware to views testing """
    middlewares = (SessionMiddleware, MessageMiddleware)
    for middleware in middlewares:
        add_middleware_to_request(request, middleware)
    return request
