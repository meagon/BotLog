

import bottle
from control.handler import LocalHandler
from bottle.ext import sqlalchemy as bottle_sql

from models.models import engine

plugin = bottle_sql.Plugin(
    engine,             # SQLAlchemy engine created with create_engine function.
    #Base.metadata,     # SQLAlchemy metadata, required only if create=True.
    keyword='db',       # Keyword used to inject session database in a route (default 'db').
    create=False,       # If it is true, execute `metadata.create_all(engine)` when plugin is applied (default False).
    commit=True,        # If it is true, plugin commit changes after route is executed (default True).
    use_kwargs=False    # If it is true and keyword is not defined, plugin uses **kwargs argument to inject session database (default False).
)


class BaseBote(bottle.Bottle):
    
    def __init__(self,*args, **kwargs):
        super(BaseBote,self).__init__(*args,**kwargs)
        self._install()


    def _install(self):
        self.install(plugin)

