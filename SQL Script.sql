CREATE DATABASE retail;

CREATE TABLE IF NOT EXISTS customer_shopping (
    customer_id INT,
    age INT,
    gender VARCHAR(10),
    location VARCHAR(50),
    category VARCHAR(50),
    item_purchased VARCHAR(100),
    size VARCHAR(10),
    color VARCHAR(30),
    season VARCHAR(20),
    purchase_amount NUMERIC(10,2),
    purchase_frequency VARCHAR(20),
    previous_purchases INT,
    discount_applied BOOLEAN,
    promo_code_used BOOLEAN,
    subscription_status BOOLEAN,
    shipping_type VARCHAR(30),
    payment_method VARCHAR(30),
    review_rating NUMERIC(3,1)
);

select * from customer_shopping;