from handler.user import UserHandler

from handler.token import TokenHandler
from handler.hello_world import HelloWorldHandler

ROUTES = [
    (r'/api/test_ansible/?$', OperationHandler),
    (r'/api/user/?', UserHandler),
    (r'/api/hello_world$', HelloWorldHandler),
]
