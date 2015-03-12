import bottle

from control.handler import  LocalHandler
from models.models import Post, Link
from control.db import BaseBote

blogs_edit_app = BaseBote()
links_edit_app = BaseBote()

@blogs_edit_app.get("/")
def addPost( db, self=LocalHandler()):
    posts = db.query(Post.title, Post.id).order_by(Post.id.desc()).all()
    return self.render('edit_blog.tpl' ) #, posts = posts)
    
@blogs_edit_app.post("/:action")
def post(action, db, self = LocalHandler()):
    if action == 'del':
        post_id = self.request.forms.get('id', 0)
        if post_id:
            post = db.query(Post).filter(Post.id == post_id)
            db.delete(post)
            db.commit()

    elif action == 'add':
        post_id = self.request.forms.get('id',0)
        post_title = self.request.forms.get('title')
        post_content = self.request.forms.get('blog-content', '')
        post_url = self.request.forms.get('title')
        post_password = self.request.forms.get('set_password','0')
        tags = self.request.forms.get('tags','')

        print(post_title, post_content, post_password)
        
        if  all((post_title, post_content)):
            """
            post = Post(id = post_id,
                    title = post_title,
                    content = post_content,
                    tags = tags,
                    type ='blogs',
                    verbose_password = post_password,
                )
            """
            post = Post(title = post_title,
                        url = post_title,
                        content = post_content
                        )
            db.add(post)
            db.commit()
    return self.redirect('/user/blog')



@links_edit_app.get("/")
def get_links( db, self = LocalHandler()):
    links = db.query(Link).all()
    self.render('links.tpl', links = links)

@links_edit_app.post("/<action>/")
def post(db, self = LocalHandler()):
    action = edit
    if action == 'add':
        name = self.requests.froms.get('name', '')
        url = self.requests.forms.get('url', '')
        if not all([name, url]):
            return self.redirect('/user/links')
        db.add(Link(name = name, url= url))
        db.commit()
        return self.redirect('/user/links')

    elif action == 'del':
        link_id = self.requests.forms.get('id', '-1')
        if link_id:
            link = db.query(Link).filter(Link.id == link_id).one()
            db.delete(link)
            db.commit()
        return self.redirect('/user/links')
