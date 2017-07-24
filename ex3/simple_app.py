from .simple_framework import simple_app, Response, Status
from pprint import PrettyPrinter

@simple_app
def application(request):
    printer = PrettyPrinter(indent=2)

    path = request.headers['PATH_INFO']
    headers = {
        'Content-Type': 'text/plain'
    }
    if path == '/':
        message = 'Hello World!'
    else:
        message = 'Goodbye World!'

    message += '\n\n' + printer.pformat(request.headers)

    return Response(Status.Ok, headers, message)
