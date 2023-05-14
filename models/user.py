from db.db import sql
import bcrypt

def create_user(first_name, last_name, email, password):
    password_digest = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    sql("INSERT INTO users(first_name, last_name, email, password_digest) VALUES(%s, %s, %s, %s) RETURNING *", [first_name, last_name, email, password_digest])


def find_user_by_email(email):
    users = sql("SELECT * FROM users WHERE email = %s", [email])
    if users:
        return users[0]
    return None
    
def find_user_by_id(user_id):
    users = sql('SELECT * FROM users WHERE user_id = %s', [user_id])
    return users[0]
