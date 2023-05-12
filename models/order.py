from db.db import sql

def update_food(id, name, image_url):
    sql('UPDATE foods SET name=%s, image_url=%s WHERE id=%s RETURNING *', [name, image_url, id])

def delete_food(id):
    sql('DELETE FROM foods WHERE id=%s RETURNING *', [id])  
