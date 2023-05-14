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