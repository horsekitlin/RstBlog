from app import db

class Blog(db.Document):
    """
    Blog DataBase

    Topic : post title
    rst : rst file name
    html : html file name
    tag : key word list
    msg : user message
    catalog : post catalog
    poster : user's uid
    date : Date
    desc : the desc of post
    """
    topic=db.StringField()
    #rst = db.StringField()
    #html = db.StringField()
    #tag = db.ListField(db.StringField())
    #msg = db.ListField(db.StringField())
    catalog = db.StringField()
    poster = db.ObjectIdField()
    date=db.DateTimeField()
    #time=db.StringField(required=True)
    desc=db.StringField()

    meta = {
        'collection': 'posts'
    }
