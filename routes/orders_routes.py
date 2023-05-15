from flask import Blueprint
from controllers.orders_controller import view, update, delete, add
from controllers.cart_controller import view_cart

orders_routes = Blueprint('orders_routes', __name__)

orders_routes.route('/<int:order_id>')(view)
orders_routes.route('/<int:order_id>/update', methods=['POST'])(update)
orders_routes.route('/<int:order_id>/delete', methods=['POST'])(delete)
orders_routes.route('/cart')(view_cart)
orders_routes.route('/cart/add', methods=['POST'])(add)