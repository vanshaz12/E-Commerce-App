from flask import render_template, request, redirect, session
from models.product import all_products, get_product, search_products, view_product, add_review, get_reviews_by_product_id
from services.session_info import current_user

def index():
    products = all_products()
    print(products)
    return render_template('products/index.html', products=products, current_user=current_user)

def search():
    search_query = request.args.get('q')
    products = search_products(search_query)
    return render_template('products/product_list.html', products=products, current_user=current_user)

def view(product_id):
    product = view_product(product_id)[0]
    print(product)
    return render_template('products/product.html', product=product, current_user=current_user)


def review(product_id):
    rating = request.form.get('rating')
    comment = request.form.get('comment')
    user_id = session['user_id']
    add_review(user_id, product_id, rating, comment)
    return redirect('/')


def view_reviews(product_id):
    reviews = get_reviews_by_product_id(product_id)
    return render_template('products/product.html', reviews=reviews)



