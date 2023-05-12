from flask import Flask, redirect
from routes.products_routes import product_routes
from routes.users_routes import users_routes
from routes.sessions_routes import sessions_routes

app = Flask(__name__)


app.register_blueprint(product_routes)
app.register_blueprint(users_routes, url_prefix = '/users')
app.register_blueprint(sessions_routes, url_prefix='/sessions')

