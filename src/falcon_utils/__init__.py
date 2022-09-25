import json
import falcon


class BaseRoute:
    URL_PATH: str = "/"
    KWARGS: dict = {}

    @classmethod
    def setup(cls, application: falcon.App):
        application.add_route(cls.URL_PATH, cls(), **cls.KWARGS)


class JSONMiddleware:
    # def process_request(self, req, resp): ...

    # def process_resource(self, req, resp, resource, params): ...

    def process_response(self, req, resp, resource, req_succeeded):
        resp.content_type = "application/json"
        if isinstance(resp.text, dict):
            resp.text = json.dumps(resp.text)


def create_routes(app):
    for route in BaseRoute.__subclasses__():
        route.setup(application)
