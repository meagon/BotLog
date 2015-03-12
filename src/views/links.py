

import bottle
from models.models import Link
from control.handler import LocalHandler
from control.db import BaseBote 


links_app = BaseBote()

@links_app.get("")
def ListLinksHandler(db , self = LocalHandler()):
    links = db.query(Link).all()
    return self.render('links.html', title = 'Friendly Links', links = links)



