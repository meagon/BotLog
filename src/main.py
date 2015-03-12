

import bottle


from views import views_app
from control.handler import LocalHandler
from control.db import BaseBote


app = BaseBote()

@app.route("/")
def index():
    return bottle.redirect("/user/blog/")

@app.route('/static/:filename#.*#')
def server_static(filename):
    return bottle.static_file(filename, root= "static")

app.mount("user", views_app )

bottle.debug(True)
app.run(reloader= True,host="0.0.0.0", port = 8888)
