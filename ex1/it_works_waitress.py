from wsgiref.simple_server import demo_app
from waitress import serve

if __name__ == '__main__':
    # From command line you can do
    # 'waitress-server --port 5000 it_works_waitress:demo_app'
    serve(demo_app, listen='*:5000')
