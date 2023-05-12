from flask import render_template, request, redirect
from models.product import all_products, get_product, search_products
from services.session_info import current_user


def index():
    products = all_products()
    return render_template('products/index.html', products=products, current_user=current_user)

def search():
    search_query = request.args.get('q')
    products = search_products(search_query)
    return render_template('products/search_results.html', products=products, current_user=current_user)

def view(product_id):
    view_product = get_product(product_id)
    return render_template('products/product.html', view_product=view_product)

