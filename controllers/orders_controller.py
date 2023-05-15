from flask import render_template, redirect, request, session
from models.order import get_order, update_order, delete_order, calculate_total_price, add_to_cart
from models.product import get_product
from services.session_info import current_user

def view(order_id):
    order = get_order(order_id)
    return render_template('order/cart.html', order=order, current_user=current_user)

def update(order_id):
    updated_order_data = {
        'order_id': order_id,
        'quantity': request.form.get('quantity'),
    }
    updated_order = update_order(updated_order_data)

    return redirect(f'/order/{updated_order.order_id}')


def delete(order_id):
    delete_order(order_id)
    return redirect('/cart')

def add(order_id):
    add_to_cart(order_id)
    return redirect('/')

    
