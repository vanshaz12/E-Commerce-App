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
    img_url TEXT,
    price TEXT,
    quantity INT
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users (user_id),
    total_amount INTEGER
);

 
CREATE TABLE cart (
    cart_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users (user_id),
    product_id INT REFERENCES products (product_id),
    quantity INT
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

INSERT INTO products (name, description, img_url, price, quantity)
VALUES
    ('Smart TV', 'High-definition smart TV with built-in streaming apps', 'https://www.lg.com/au/images/tvs/md07548633/gallery/D-2s.jpg', '799.99', 10),
    ('Laptop', 'Powerful laptop with fast processor and ample storage', 'https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE4LJcl?ver=3fd0&q=90&m=6&h=705&w=1253&b=%23FFFFFFFF&f=jpg&o=f&p=140&aim=true', '1299.99', 5),
    ('Wireless Headphones', 'Premium wireless headphones with noise cancellation', 'https://www.sony.com.au/image/6145c1d32e6ac8e63a46c912dc33c5bb?fmt=pjpeg&bgcolor=FFFFFF&bgc=FFFFFF&wid=2515&hei=1320', '249.99', 20),
    ('Bluetooth Speaker', 'Portable Bluetooth speaker with high-quality sound', 'https://cdn.shopify.com/s/files/1/0561/9535/0689/products/BT9330-2020.jpg?v=1623032500', '99.99', 15),
    ('Digital Camera', 'Advanced digital camera with professional features', 'https://example.com/images/camera.jpg', '899.99', 8),
    ('Gaming Console', 'Next-generation gaming console for immersive gaming experiences', 'https://gmedia.playstation.com/is/image/SIEPDC/ps5-console-covers-keyart-01-en-08dec21?$facebook$', '499.99', 3),
    ('Smartphone', 'Latest smartphone with advanced features and high-resolution display', 'https://example.com/images/smartphone.jpg', '899.99', 12),
    ('Tablet', 'Versatile tablet for work, entertainment, and productivity', 'https://example.com/images/tablet.jpg', '599.99', 7),
    ('Wireless Router', 'High-speed wireless router for seamless internet connectivity', 'https://example.com/images/router.jpg', '129.99', 10),
    ('Smart Watch', 'Smartwatch with fitness tracking and notification features', 'https://example.com/images/smart_watch.jpg', '199.99', 18);




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