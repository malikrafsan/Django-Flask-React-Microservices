from werkzeug.wrappers import Request, Response
import os

class APIKeyMiddleware:
    def __init__(self, app):
        self.app = app
        self.api_key = os.getenv('API_KEY')
        print('API_KEY: %s' % self.api_key)

    def __call__(self, environ, start_response):
        request = Request(environ)
        print(f"path: {request.path}, method: {request.method}")
        print(f"headers: {request.headers}")

        api_key = request.headers.get('X-API-KEY')
        print("api_key", api_key)
        if api_key is None:
            res = Response({'message': 'Missing API key'}, status=401)
            return res(environ, start_response)

        if api_key != self.api_key:
            res = Response({'message': 'Invalid API key'}, status=401)
            return res(environ, start_response)

        return self.app(environ, start_response)
