""" Helper functions to facilitate testing """


def add_middleware_to_request(request, middleware_class):
    """
    Supports a testing scenario which simulates an active middleware
    session within the lifecycle of a request.
    """
    middleware = middleware_class()
    middleware.process_request(request)
    request.session.save()
    return request
