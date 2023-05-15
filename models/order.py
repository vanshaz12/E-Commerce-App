from db.db import sql

def get_order(order_id):
    result = sql("SELECT * FROM orders WHERE order_id = %s", [order_id])
    if result:
        return result[0]
    return None

def update_order(order_data):
    sql("UPDATE orders SET quantity = %s, address = %s WHERE order_id = %s",
        [order_data['quantity'], order_data['address'], order_data['order_id']])
    return get_order(order_data['order_id'])


def delete_order(order_id):
    sql("DELETE FROM orders WHERE order_id = %s", [order_id])



