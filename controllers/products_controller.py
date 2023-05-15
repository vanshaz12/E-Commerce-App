from flask import render_template, request
from models.product import all_products, get_product, search_products, view_product
from services.session_info import current_user

def index():
    products = all_products()
    return render_template('products/index.html', products=products, current_user=current_user)

def search():
    search_query = request.args.get('q')
    products = search_products(search_query)
    return render_template('products/product_list.html', products=products, current_user=current_user)

def view(product_id):
    product = view_product(product_id)[0]
    print(product)
    return render_template('products/product.html', product=product, current_user=current_user)


