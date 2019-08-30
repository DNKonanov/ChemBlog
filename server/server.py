from flask import Flask, jsonify, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/home/')
def answer():
    return render_template('pages/index.html')

@app.route('/posts/')
def posts():

    #will be loaded from DB
    posts = [
        {
            'id': 0,
            'title': 'First',
            'short_desc': 'Short desc of the First',
            'author': 'admin',
            'date': '01.01.2020'
        },
        {
            'id': 1,
            'title': 'Second',
            'short_desc': 'Short desc of the Second',
            'author': 'user',
            'date': '06.06.2020'
        }
    ]

    return render_template('pages/posts.html', posts=posts)

@app.route('/about/')
def about():
    return render_template('pages/about.html')

@app.route('/posts/<int:id>')
def show_post(id=0):

    #will be loaded from DB by id
    article_header = 'Phenylalanine'
    article_text = 'Phenylalanine is an essential aromatic amino acid in humans (provided by food), Phenylalanine plays a key role in the biosynthesis of other amino acids and is important in the structure and function of many proteins and enzymes.'
    return render_template('pages/post.html', article_text=article_text, article_header=article_header)



app.run()