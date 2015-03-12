
from bottle import request, response, HTTPError, redirect
from jinja2 import Environment, FileSystemLoader, TemplateNotFound

class LocalHandler(object):
        
    settings = {}

    def __init__(self, *args, **kwargs):
        self.request = request
        self.response = response
        self.HTTPError = HTTPError
        self.prepare()

    @classmethod
    def prepare(cls, path="template_path", value ="tempalte"):
        cls.settings.setdefault(path, value)

    
    def set_path(self, path="template_path", value = "template"):
        self.settings.__setitem__( path, value)
    
    def render(self, template_name, **kwargs):
        return self._render( "templates", template_name, **kwargs)

    def _render(self, _dir, template_name, **kwargs):
        env = Environment(loader = FileSystemLoader(_dir))
        try:
            template = env.get_template(template_name)
        except TemplateNotFound:
            raise TemplateNotFound(template_name)
        return template.render( local =self.settings, **kwargs)
    
    def _jinja2_render(self, template_name, **kwargs):
        return self._render(self.settings['template_path'], template_name, **kwargs)

    def backend_render(self, template_name, **kwargs):
        return self._render(self.settings['template_path'], template_name, **kwargs)

    def redirect(self, url , code = None):
        redirect(url, code = code)
