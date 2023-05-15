from db.db import sql

def all_products():
    return sql('SELECT * FROM products')

def get_product(product_id):
    product = sql('SELECT * FROM products WHERE id = %s', [product_id])
    return product[0] if product else None

def search_products(search_query):
    search_query = '%' + search_query + '%'
    products = sql('SELECT * FROM products WHERE name ILIKE %s', [search_query])
    return products

def view_product(product_id):
    query = "SELECT * FROM products WHERE product_id = %s"
    view_product = sql(query, [product_id])
    return view_product

def add_review(user_id, product_id, rating, comment):
    sql("INSERT INTO reviews (user_id, product_id, rating, comment) VALUES (%s, %s, %s, %s), RETURNING *", [user_id, product_id, rating, comment])
