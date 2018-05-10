from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

posts_tags = db.Table('posts_tags',
    db.Column('post_id', db.String(45), db.ForeignKey('posts.id')),
    db.Column('tag_id', db.String(45), db.ForeignKey('tags.id')))

class User(db.Model):
    '''users'''

    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    # Establish contact with Post's ForeignKey: user_id
    posts = db.relationship(
        'Post',
        backref = 'users',
        lazy = 'dynamic'
    )

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return "<Model User> '{}'".format(self.username)

    @property
    def password(self):
        raise AttributeError('password is not readable')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):

    __tablename__ = 'posts'
    id = db.Column(db.String(45), primary_key = True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime)
    # Set the foreign key for Post
    user_id = db.Column(db.String(45), db.ForeignKey('users.id'))
    # Establish contact with Comment's ForeignKey: post_id
    comments = db.relationship(
        'Comment',
        backref = 'posts',
        lazy = 'dynamic',
    )
    # many to many: posts <==> tags
    tags = db.relationship(
        'Tag',
        secondary = posts_tags,
        backref = db.backref('posts', lazy = 'dynamic')
    )

    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __repr__(self):
        return "<Moel Post '{}'>".format(self.title)


class Tag(db.Model):

    __tablename__ = 'tags'
    id = db.Column(db.String(45), primary_key = True)
    name = db.Column(db.String(255))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Model Tag '{}'".format(self.name)

class Comment(db.Model):

    __tablename__ = 'comments'
    id = db.Column(db.String(45), primary_key = True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.String(45), db.ForeignKey('posts.id'))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Model Comment {}>".format(self.name)
