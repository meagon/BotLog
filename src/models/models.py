#-*- coding:utf-8 -*-

from datetime import date
from hashlib import md5

from sqlalchemy import create_engine
from sqlalchemy import Column,Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Text, String, Date, Integer, ForeignKey, Enum

from sqlalchemy.orm import exc


NotResultFound = exc.NoResultFound

Base = declarative_base()

local_db_info = 'postgresql://postgres:postgres@127.0.0.1:5432/blog'
engine = create_engine(local_db_info, echo = True)


POST_CATEGORIES = ('article', 'personal', )

posts_tags = Table(
    'posts_tags', Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id')),
    Column('tag_id', Integer, ForeignKey('tags.id')),
)


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    username = Column(String(20))
    password = Column(String(32))  # md5 length  32
    
    def auth_ok(self, password):
        return self.password == md5(password).hexdigest()
    def __repr__(self):
        return '<User: %s>' %self.username
       
class Tag(Base):
    __tablename__ ='tags'
    id = Column(Integer, primary_key = True, autoincrement = True)
    mark = Column(String(50), unique = True, nullable = False)
    
    def __repr__(self):
        return '<Tag: %s>' %self.mark
    
class Post(Base):
    __tablename__ ='posts'
 
    id = Column(Integer, primary_key = True, autoincrement= True)
    title = Column(String(200), unique = True, nullable =False)
    url = Column(String(200), unique = True, nullable = False ) #  for english title
    tags  = relationship('Tag', secondary = posts_tags, backref = 'posts')
    created_date = Column(Date, default= date.today())  # in sqltypes.py Date just like datetime.date
    content = Column(Text)
    type = Column(Enum(*POST_CATEGORIES, name='post_category'))
    verbose_password = Column(String(10), nullable = True)

    def __repr__(self):
        return '<Post %s>' %self.title

class Link(Base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(120))
    url  = Column(String(120))
    
    def __repr__(self):
        return '<Link %s>'  %self.url
        
def init_db():
    local_db_info = 'postgresql://postgres:postgres@127.0.0.1:5432/blog'
    engine = create_engine(local_db_info, echo = True)
    metadata = Base.metadata
    metadata.create_all(engine)

if __name__ == '__main__':
    init_db()
