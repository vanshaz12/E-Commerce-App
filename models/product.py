from db.db import sql

def all_products():
    return sql('SELECT * FROM prodcuts ORDER BY id')

def get_product(id):
    products = sql("SELECT * FROM prodcuts WHERE id = %s", [id])
    return products[0]

  
            