from flask import Flask, render_template
import os

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/articles')
def articles():
    articles = os.listdir('markdowns')
    articles = map(lambda x: x[:-3],articles)
    articles.remove('index')
    return render_template('articles.html',articles=articles)

@app.route('/articles/<name>')
def show_article(name):
    return app.send_static_file(name+'.html')
