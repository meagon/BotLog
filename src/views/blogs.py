#-*- encoding:utf-8 -*-

import itertools
from sqlalchemy.orm.exc import NoResultFound
import sys

#sys.path.append("../models")
from models.models  import Post, Tag
from control.db import BaseBote
from control.handler import LocalHandler

blog = BaseBote()

@blog.get("/")
@blog.get("/<page>/")
def recentPostsHandler(db, page=1, self=LocalHandler()):
    page = int(page)
    posts = db.query(Post).order_by(Post.id.desc()).limit(1).offset((page-1)*3).one()
    
    print(type(posts))
    #posts[0]

    return self.render('index.html',
            title = "Meagon Blog Page",
            data = {
                'post': posts ,
            },
            post = posts)

@blog.get("/title/<title>")
def SpicialTitleHandler( title, db, self=LocalHandler()):
    try:
        post = db.query(Post).filter(and_(Post.title == title, Post.type == 'blog')).one()
    except NoResultFound:
        return self.redirect('/seven')

    return self.render('blog.html', title=post.title, post = post)


@blog.get("/tag/<tagName>")
def SpecialTagHandler(tagName, db , self = LocalHandler()):
    try:
        tag = db.query(Tag).filter(Tag.mark == tagName).one()
    except NoResultFound:
        return self.redirect('/seven')

    posts = [post for post in tag.post if post.type == constants.POST]

    return self.render('index.html',title = 'Tag: %s' %tag.tagName, data={
            'preview':0,
            'next': 0,
            'posts': posts,
        })


@blog.get("/archive")
def archiveHandler(db, self = LocalHandler()):
    posts = db.query(Post.title, Post.created_date).filter(Post.type == 'article').order_by(Post.id.desc()).all()

    print(type(posts[0].created_date))
    post_archives = [{'year': year, 'posts':list(posts)} for year, posts in
        itertools.groupby(posts, key= lambda post: post.created_date.year)]

    return self.render('archives.tpl', title ='Archives', post_archives = post_archives)


