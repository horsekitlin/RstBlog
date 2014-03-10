"""
Author:Tomas
Date:2014-03-05
Desc : Blog View
"""
from flask import (Blueprint, render_template, \
        request, redirect, url_for)
from app.models import Blog
from mongoengine.base import ValidationError
from flask.views import MethodView

blog = Blueprint("blog", __name__, template_folder='templates')

class ListView(MethodView):
    def get(self):
        posts = Blog.objects
        return render_template('blog/index.html', posts=posts)

class CreateView(MethodView):
    def get(self):
        return render_template('blog/create.html')

    def post(self):
        get_dict = lambda dct, *keys: {key:dct[key] for key in keys}
        post = get_dict(request.form, 'topic', 'date', 'catalog', 'desc')
        try:
            Blog(**post).save()
        except:
            return redirect(url_for('blog.list', error='Inser Fail!'))
        return redirect(url_for('blog.list'))

class ShowPostView(MethodView):
    def get(seld):
        pass


blog.add_url_rule('/', view_func = ListView.as_view('list'))
blog.add_url_rule('/create', view_func = CreateView.as_view('create'))
