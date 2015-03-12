
from base import *

class Post(Base):
    
    __tablename__ ='posts'

    id = Column(Integer,primary_key = True, autoincrement= True)
    title = Column(String(200), unique = True, nullable =False)
    url = Column(String(200), unique = True, nullable = False ) #  for english title
    tags  = relationship('Tag', secondary = posts_tags, backref = 'posts')
    created_date = Column(Date, default= date.today())  # in sqltypes.py Date just like datetime.date
    content = Column(Text)
    type = Column(Enum(*POST_CATEGORIES, name='post_category'))
    verbose_password = Column(String(10), nullable = True)

    def __repr__(self):
        return '<Post %s>' %self.title

    """
    def __init__(self,title = title, url = url, tags= tags, content = None ,verbose_password = "0"):
        self.title = title
        self.content = content or ""
        self.tags = tags
        self.verbose_password = verbose_password
    """
