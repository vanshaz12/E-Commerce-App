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
    
    if len(existing_order) > 0:
        print("in if")
        # Update the existing order by adding the new item to the cart
        sql('INSERT INTO cart (user_id, product_id, quantity) VALUES (%s, %s, %s)',
            [user_id, product_id, quantity])
    else:
        print("in esle")
        user_id = session.get("user_id")
        # Create a new order and add the item to the cart
        sql('INSERT INTO cart (user_id, product_id, quantity) VALUES (%s, %s, %s)',
            [user_id, product_id, quantity])







