from flask import Flask, jsonify, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/home/')
def answer():
    return render_template('index.html')

@app.route('/posts/')
def posts():
    return render_template('posts.html')


app.run()