from dotenv import load_dotenv
load_dotenv()

import os
import requests
from flask import Flask, redirect
from routes.products_routes import product_routes
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
Flask.secret_key = 'shjcsjvchjsvj^%^FVHvt6&RYCyd6'


app = Flask(__name__)

app.config['GOOGLE_API_KEY'] = GOOGLE_API_KEY

app.register_blueprint(product_routes)
app.register_blueprint(users_routes, url_prefix = '/users')
app.register_blueprint(sessions_routes, url_prefix='/sessions')

@app.route('/')
def index():
    return redirect('/index')
