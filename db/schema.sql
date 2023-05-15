CREATE DATABASE e_comm_db;
\c e_comm_db


CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT
    );

CREATE TABLE products(
    product_id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT,
    img_url TEXT
    price TEXT,
    quantity INT
);

CREATE TABLE orders(
    order_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    order_date TEXT,
    total_amount INT
);

CREATE TABLE cart(
    order_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    order_date TEXT,
    total_amount INT
);

CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    product_id INT,
    user_id INT,
    rating INT,
    comment TEXT,
    FOREIGN KEY (product_id) REFERENCES products (product_id),
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);