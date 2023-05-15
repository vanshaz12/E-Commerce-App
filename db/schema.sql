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

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id REFERENCES users (user_id),
    total_amount INTEGER,
    cart_items JSONB
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



--  product_id |        name         |                             description                              |  price  | quantity |                  img_url
-- ------------+---------------------+----------------------------------------------------------------------+---------+----------+--------------------------------------------
--           1 | Smart TV            | High-definition smart TV with built-in streaming apps                | 799.99  |       10 | https://example.com/images/smart_tv.jpg
--           2 | Laptop              | Powerful laptop with fast processor and ample storage                | 1299.99 |        5 | https://example.com/images/laptop.jpg
--           3 | Wireless Headphones | Premium wireless headphones with noise cancellation                  | 249.99  |       20 | https://example.com/images/headphones.jpg
--           4 | Bluetooth Speaker   | Portable Bluetooth speaker with high-quality sound                   | 99.99   |       15 | https://example.com/images/speaker.jpg
--           5 | Digital Camera      | Advanced digital camera with professional features                   | 899.99  |        8 | https://example.com/images/camera.jpg
--           6 | Gaming Console      | Next-generation gaming console for immersive gaming experiences      | 499.99  |        3 | https://example.com/images/console.jpg
--           7 | Smartphone          | Latest smartphone with advanced features and high-resolution display | 899.99  |       12 | https://example.com/images/smartphone.jpg
--           8 | Tablet              | Versatile tablet for work, entertainment, and productivity           | 599.99  |        7 | https://example.com/images/tablet.jpg
--           9 | Wireless Router     | High-speed wireless router for seamless internet connectivity        | 129.99  |       10 | https://example.com/images/router.jpg
--          10 | Smart Watch         | Smartwatch with fitness tracking and notification features           | 199.99  |       18 | https://example.com/images/smart_watch.jpg