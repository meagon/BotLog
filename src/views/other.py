
import bottle
from control.handler import LocalHandler
from control.db import BaseBote

other_app = BaseBote()

@other_app.get("/*")
def NotFoundHandler(self = LocalHandler()):
    return self.render('not_found.html', title = '404 Not Found')

@other_app.get("/seven") 
def seven_get(self=LocalHandler()):
    return self.render('where_is_kaid.html', title="where is kaid")


