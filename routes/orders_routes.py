from flask import Blueprint
from controllers.orders_controller import view, update, delete

orders_routes = Blueprint('orders_routes', __name__)

orders_routes.route('/orders/<int:order_id>')(view)
orders_routes.route('/orders/<int:order_id>/update', methods=['POST'])(update)
orders_routes.route('/orders/<int:order_id>/delete', methods=['POST'])(delete)
