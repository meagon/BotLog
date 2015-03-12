from hashlib import md5

from models.models import User, NotResultFound
from control.handler import LocalHandler
from control.db import BaseBote


login_app = BaseBote()
    
@login_app.get("/")
def getLogin(self = LocalHandler()):
    #return "login"
    return self.render('login.tpl', title = 'Login')

@login_app.post("/")
def postLogin(db, self = LocalHandler()):
    username = self.request.forms.get('username')
    password = self.request.forms.get('password')
    
    if username and password:
        try:
            user = db.query(User).filter(User.username == username).one()
        except NotResultFound:
            self.redirect('/user/login')

        if len(password) != 32:
            password = md5(password).hexdigest()
        if user.auth_ok(password):
            self.request.set_cookie('username', user.username)
            self.redirect('/user/')

    return self.redirect('/user/login')

user_app = BaseBote()

@user_app.get("/")
def get_user(self = LocalHandler()):
    username = self.settings.get("username")
    self.render("profile.tpl")

