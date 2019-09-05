from handler.base import BaseHandler


class HelloWorldHandler(BaseHandler):
    def get(self, *args, **kwargs):
        res = {"text": "Hello World !"}
        self.render_json_response(code=200, msg='OK', res=res)
