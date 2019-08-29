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
    return render_template('pages/posts.html')

@app.route('/about/')
def about():
    return render_template('pages/about.html')

app.run()