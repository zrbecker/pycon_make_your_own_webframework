# Implements a simple request and response framework for wsgi

from functools import wraps

class Status:
    def __init__(self, code, desc):
        self.code = code
        self.desc = desc

    def __str__(self):
        return '{} {}'.format(self.code, self.desc)

Status.Ok = Status(200, 'OK')
Status.NotFound = Status(404, 'Not Found')
Status.MovedPermanently = Status(301, 'Moved Permanently')

class Request:
    def __init__(self, wsgi_environ):
        headers = {}
        for k, v in wsgi_environ.items():
            if not k.startswith('wsgi.'):
                headers[k] = v
        self.headers = headers

class Response:
    def __init__(self, status, headers, body, encoding='utf-8'):
        self.status = status
        self.headers = [(k, v) for k, v in headers.items()]
        self.body = body
        self.encoding = encoding

def simple_app(f):
    @wraps(f)
    def decorated(environ, start_response):
        request = Request(environ)
        response = f(request)
        start_response(str(response.status), response.headers)
        return [response.body.encode(response.encoding)]
    return decorated
