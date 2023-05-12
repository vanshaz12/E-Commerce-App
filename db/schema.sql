CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT
    );

CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT,
    price TEXT,
    quantity INT
);

CREATE TABLE orders(
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    order_date TEXT,
    total_amount INT
);