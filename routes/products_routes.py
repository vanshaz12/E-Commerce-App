from flask import Blueprint
from controllers.products_controller import index, view, search

product_routes = Blueprint('products_routes', __name__)

product_routes.route('/')(index)
product_routes.route('/product/<int:product_id>')(view)
product_routes.route('/search')(search)