from werkzeug.wrappers import Request, Response
import os

class APIKeyMiddleware:
    def __init__(self, app):
        self.app = app
        self.api_key = os.getenv('API_KEY')
        print('API_KEY: %s' % self.api_key)

    def __call__(self, environ, start_response):
        request = Request(environ)
        print('path: %s, url: %s' % (request.path, request.url))

        api_key = request.headers.get('X-API-KEY')
        print(request.headers)
        if api_key is None:
            res = Response(u'API key is missing',
                           mimetype='text/plain', status=401)
            return res(environ, start_response)

        if api_key != self.api_key:
            res = Response(u'API key is invalid',
                           mimetype='text/plain', status=401)
            return res(environ, start_response)

        return self.app(environ, start_response)
