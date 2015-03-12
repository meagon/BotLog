


import bottle
import views
import secure

from bottle import HTTPError
app = bottle.app()

"""
for path, method in views.handlers:
    app.add_route(path, method)
"""


class BaseHandler(bottle.request, bottle.response, secure.SecretCookie):
    
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)
        
        self.request = request
        

    def redirect(self):
        return bottle.redirect(url, code=None)

   
    
