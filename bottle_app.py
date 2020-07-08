
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, post, get, template

import sqlite3
db=sqlite3.connect("./mysite/nfl.db")
c=db.cursor()


@route('/')
def index():
    return template("index.html", c=c)

@post('/results')
def getWings():
    return template("results.html", c=c)



application=default_app()