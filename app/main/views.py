from uuid import uuid4
from datetime import datetime
from os import path
from flask import render_template
from sqlalchemy import func

from app.models import db, User, Post, Tag, Comment, posts_tags
from app.main.forms import CommentForm
from . import main



def sidebar_data():
    '''Set the sidebar function'''

    # Get post of recent
    recent = db.session.query(Post).order_by(
        Post.publish_date.desc()
    ).limit(5).all()

    # Get the tags and sort by count of posts.
    top_tags = db.session.query(
        Tag, func.count(posts_tags.c.post_id).label('total')
    ).join(
        posts_tags
    ).group_by(Tag).order_by('total DESC').limit(5).all()

    return recent, top_tags

@main.route('/')
@main.route('/<int:page>')
def home(page=1):
    '''View func for homepage'''

    posts = Post.query.order_by(
        Post.publish_date.desc()
    ).paginate(page, 10)

    recent, top_tags = sidebar_data()

    return render_template('home.html',
                            posts=posts,
                            recent=recent,
                            top_tags=top_tags)

@main.route('/post/<string:post_id>', methods=('GET', 'POST'))
def post(post_id):
    '''view func for post page'''

    # From obj: 'Comment'
    form = CommentForm()
    # form.validate_on_submit() will be true and return the data obj
    # to form instance from user enter, when HTTP request is POST
    if form.validate_on_submit():
        new_comment = Comment(id=str(uuid4()),
                              name=form.name.data)
        new_comment.text = form.text.data
        new_comment.date = datetime.datetime.now()
        new_comment.post_id = post_id
        db.session.add(new_comment)
        db.session.commit()

    post = db.session.query(Post).get_or_404(post_id)
    tags = post.tags
    comments = post.comments.order_by(Comment.date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template('post.html',
                            post=post,
                            tags=tags,
                            comments=comments,
                            recent=recent,
                            top_tags=top_tags,
                            form=form)

@main.route('/tag/<string:tag_name>')
def tag(tag_name):
    """View function for tag page"""

    tag = db.session.query(Tag).filter_by(name=tag_name).first_or_404()
    posts = tag.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template('tag.html',
                           tag=tag,
                           posts=posts,
                           recent=recent,
                           top_tags=top_tags)


@main.route('/user/<string:username>')
def user(username):
    """View function for user page"""
    user = db.session.query(User).filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template('user.html',
                           user=user,
                           posts=posts,
                           recent=recent,
                           top_tags=top_tags)
