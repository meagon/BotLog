import  bottle

from bottle.ext import sqlalchemy as bottle_sql
from control.db import BaseBote
from models.models import engine


__all__ = ["views_app"]

from blogs import blog
from links import links_app
from edit import links_edit_app, blogs_edit_app
from backend import  login_app, user_app
from other import other_app

views_app = BaseBote()

views_app.mount("blog", blog)
views_app.mount("links", links_app)
views_app.mount("user", user_app)
views_app.mount("login", login_app)
views_app.mount("other", other_app)
views_app.mount("edit", blogs_edit_app)
views_app.mount("edit/links", links_edit_app)


@views_app.get("/")
def index():
    return "view_app"

