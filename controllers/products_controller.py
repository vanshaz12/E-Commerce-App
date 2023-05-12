from flask import render_template, request, redirect
from models.product import all_products, get_product
from services.session_info import current_user


def index():
    products = all_products()
    return render_template('products/index.html', products=products, current_user=current_user)

def view():
    view_product = get_product()
    return render_template('products/new.html')

def create():
    name = request.form.get('name')
    description = request.form.get('description')
    price = float(request.form.get('price'))
    quantity = int(request.form.get('quantity'))
    create_product(name, description, price, quantity)
    return redirect('/')

def edit(id):
    product = get_product(id)
    return render_template('products/edit.html', product=product)

def update(id):
    name = request.form.get('name')
    description = request.form.get('description')
    price = float(request.form.get('price'))
    quantity = int(request.form.get('quantity'))
    update_product(id, name, description, price, quantity)
    return redirect('/')

def delete(id):
    delete_product(id)
    return redirect('/')
