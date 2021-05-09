from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

@app.context_processor
def inject_user():
    user = User.query.first()
    return dict(user=user)

@app.route('/')
@app.route('/home')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

@app.route('/user/<name>')
def user_page(name):
    return name

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Config SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path, 'data.db') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))
