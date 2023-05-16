from db.db import sql
from flask import session, request, url_for, redirect, render_template
from models.product import get_product


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

def view_cart():
    cart = session.get('cart', [])
    total_price = calculate_total_price(cart)
    return render_template('products/cart.html', cart=cart, total_price=total_price)
    
def add_to_cart(user_id, product_id, quantity):
    user_id = session.get('user_id')

    # Check if the user already has an existing cart
    existing_cart = sql('SELECT * FROM cart WHERE user_id = %s', [user_id])

    if existing_cart:
        # Update the existing cart by adding the new item
        sql('INSERT INTO cart (user_id, product_id, quantity) VALUES (%s, %s, %s) RETURNING *',
            [user_id, product_id, quantity])
    else:
        # Create a new cart and add the item to it
        sql('INSERT INTO cart (user_id, product_id, quantity) VALUES (%s, %s, %s) RETURNING *',
            [user_id, product_id, quantity])

    # return redirect('/')







