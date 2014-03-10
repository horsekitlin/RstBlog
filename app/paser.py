#-*- coding:utf-8 -*-
from flask import (Blueprint, render_template, \
        request, redirect, url_for)
#from app.models import Blog
#from mongoengine.base import ValidationError
from docutils.core import publish_parts
from os.path import dirname
from time import time, strftime, localtime
from datetime import datetime

paser = Blueprint("paser", __name__, template_folder='templates')

@paser.route('/paser/tohtml')
def tohtml():
    """
    rst to html
    """

    rstpath = '{}/data/mongodb.rst'.format(dirname(__file__))
    now = strftime('%Y-%m-%d %H:%M:%S', localtime(time()))
    rst = open(rstpath, 'r')
    html = publish_parts(rst.read(),writer_name='html')
    htmlpath = '{}/data/{}.html'.format(dirname(__file__), now.split(' ')[0])
    htmlfile = open(htmlpath, 'w')
    html["html_body"] = u"<body>\n{}</body>\n".format(html["html_body"])
    html["html_head"] = u"<head>\n{}</head>\n".format(html["html_head"])
    content = u'<!DOCTYPE html>\n<html>\n{}{}</html>'.format(html["html_head"], html["html_body"])
    htmlfile.write(content)
    htmlfile.close()
    rst.close()
    return 'aaa'
