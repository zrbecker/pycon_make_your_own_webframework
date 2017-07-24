
def hello_pycon(environ, start_response):
    args = {}
    if len(environ['QUERY_STRING']) > 0:
        for arg in environ['QUERY_STRING'].split('&'):
            kvp = arg.split('=')
            if len(kvp) == 1:
                args[kvp[0]] = True
            else:
                args[kvp[0]] = '='.join(kvp[1:])

    name = args['name'] if 'name' in args else 'World'
    message = 'Hello {}!'.format(name)

    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    encoding = 'utf-8'

    start_response(status, headers)
    return [message.encode(encoding)]
