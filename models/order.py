from db.db import sql
from flask import session, request, url_for, redirect


def get_order(order_id):
    result = sql("SELECT * FROM orders WHERE order_id = %s", [order_id])
    if result:
        return result[0]
    return None

def update_order(order_data):
    sql("UPDATE orders SET quantity = %s, address = %s WHERE order_id = %s",
        [order_data['quantity'], order_data['address'], order_data['order_id']])
    return get_order(order_data['order_id'])


def delete_order(order_id):
    sql("DELETE FROM orders WHERE order_id = %s", [order_id])


def calculate_total_price(cart):
    total_price = 0
    
    for item in cart:
        product = item['product']
        quantity = item['quantity']
        price = product.price
        subtotal = price * quantity
        total_price += subtotal
    
    return total_price

def add_to_cart(user_id, product_id, quantity):
    # Check if the user already has an existing order
    existing_order = sql('SELECT * FROM orders WHERE user_id = %s', [user_id])
    if existing_order:
        # Update the existing order by adding the new item
        sql('UPDATE orders SET cart_items = jsonb_set(cart_items, \'{{%s}}\', \'%s\', true) WHERE user_id = %s',
            [product_id, quantity, user_id])
    else:
        # Create a new order with the new item
        sql('INSERT INTO orders (user_id, cart_items) VALUES (%s, jsonb_build_object(%s, %s))',
            [user_id, product_id, quantity])





