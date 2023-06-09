from dotenv import load_dotenv
load_dotenv()

import os
import requests
from flask import Flask, redirect, session, request, flash, url_for
from db.db import sql
from routes.products_routes import product_routes
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes
from routes.orders_routes import orders_routes

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
Flask.secret_key = 'shjcsjvchjsvj^%^FVHvt6&RYCyd6'


app = Flask(__name__)

app.config['GOOGLE_API_KEY'] = GOOGLE_API_KEY

app.register_blueprint(product_routes, url_prefix = '/products')
app.register_blueprint(users_routes, url_prefix = '/users')
app.register_blueprint(sessions_routes, url_prefix='/sessions')
app.register_blueprint(orders_routes, url_prefix = '/orders')
@app.route('/')
def index():
    return redirect('/products')



