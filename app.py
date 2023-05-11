from flask import Flask, redirect
from routes.users_routes import users_routes

app = Flask(__name__)

app.register_blueprint(users_routes, url_prefix = '/users')