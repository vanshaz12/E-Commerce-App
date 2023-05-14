from flask import render_template, redirect, request
from models.order import get_order, update_order, delete_order
from services.session_info import current_user

def view(order_id):
    order = get_order(order_id)
    return render_template('order/view.html', order=order, current_user=current_user)

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