from flask import Blueprint
from controllers.products_controller import index, view, search, review
from controllers.orders_controller import add

product_routes = Blueprint('products_routes', __name__)

product_routes.route('/', methods=['GET'])(index)
product_routes.route('/<int:product_id>', methods=['GET', 'POST'])(view)
product_routes.route('/search', methods=['GET'])(search)
product_routes.route('/<int:product_id>/reviews', methods=["POST"])(review)



