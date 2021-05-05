from flask import Flask, render_template, request, redirect
from request import *
from sqlalchemy import *
from flask_sqlalchemy import SQLAlchemy
from typing import Callable


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///forum.db'

class MySQLAlchemy(SQLAlchemy):  # Or you can add the below code on the SQLAlchemy directly if you think to modify the package code is acceptable.
    Column: Callable  # Use the typing to tell the IDE what the type is.
    String: Callable
    Integer: Callable
    text: Callable
db=MySQLAlchemy(app)



class Page(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    topic=db.Column(db.String)
    amount=db.Column(db.Integer)
    coll=db.Column(db.String)
   # about=db.Column(db.String)

    def __repr__(self):
        return '<Page %r>' % self.id


with app.app_context():
    db.create_all()

@app.route('/')
def hello_world():
    return render_template("first.html")


@app.route('/create', methods=['POST','GET'])
def create():
    if request.method=="POST":
        #  url="http://ratmania.ru/forum/index.php?board=50.0"
        url=request.form['url']
        http = []
        # urls=get_urls(url)

        # for i in urls:
        #   http.append(i)

        http.append(url)

        http.append("http://ratmania.ru/forum/index.php?topic=25303.0")

        array = analise_more(http)
        av = page_info(array)
        for i in array:
            page=Page(topic=i[0],amount=i[1],coll=i[2])

        try:
            db.session.add(page)
            db.session.commit()
            return redirect('/')
        except:
            print("Oh no darling")
    else:
        return render_template("create.html")


@app.route('/post')
def posts():
    pages=Page.query.order_by(Page.amount).all()
    return render_template("post.html", pages=pages)


if __name__ == '__main__':
    app.run()
