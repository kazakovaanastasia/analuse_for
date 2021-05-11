from flask import Flask, render_template, request, redirect
from request import *
from sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy
from typing import Callable

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'


class MySQLAlchemy(
    SQLAlchemy):
    Column: Callable
    String: Callable
    Integer: Callable
    text: Callable


db = MySQLAlchemy(app)


class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String)
    amount = db.Column(db.Integer)
    coll = db.Column(db.String)
    ref = db.Column(db.String,default="ss")

    # about=db.Column(db.String)

    def __repr__(self):
        return '<Page %r>' % self.id


with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():
    return render_template("first.html")


@app.route('/about')
def info():
    return render_template("about.html")


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == "POST":
        url = request.form['url']
        topic=request.form['topic']
        ref=str(url)
        http = []
        urls = get_urls(url)

        for i in urls:
            http.append(i)

        array = analise_more(http)
        av = int(page_info(array))
        name=page_name(array)
        name_count = page_mes(array)
        name+="  "
        name+=str(name_count)

        page = Page(topic=topic, amount=av, coll=name, ref=ref)
        try:
            db.session.add(page)
            db.session.commit()
        except:
            print("Oh no darling")
        return redirect('/post')

    else:
        return render_template("create.html")


@app.route('/post')
def posts():
    pages = Page.query.order_by(Page.amount).all()
    return render_template("post.html", pages=pages)


if __name__ == '__main__':
    app.run()
