from flask import render_template, redirect, request, session
from models.order import calculate_total_price
from models.product import get_product
from services.session_info import current_user



def add_to_cart(product_id):
    quantity = int(request.form.get('quantity'))
    product = get_product(product_id)
    cart_item = {
        'product': product,
        'quantity': quantity
    }
    if 'cart' in session:
        cart = session['cart']
    else:
        cart = []
    cart.append(cart_item)
    session['cart'] = cart
    return redirect('/')

def view_cart():

    cart = session.get('cart', [])

    total_price = calculate_total_price(cart)
    
    return render_template('products/cart.html', cart=cart, total_price=total_price)