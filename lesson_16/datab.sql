CREATE DATABASE Nutrition_tracker OWNER billy ENCODING = 'UTF8';
CREATE TABLE "user"
(   id      SERIAL PRIMARY KEY, --unique id
    name    VARCHAR(50) NOT NULL, --user name can't be empty
    email   VARCHAR(100) UNIQUE NOT NULL -- unique and can't be empty
);
CREATE TABLE "product"
(
    id       SERIAL PRIMARY KEY,      --unique id
    name     VARCHAR(50) NOT NULL,    --name of product can't be empty
    category VARCHAR(50),             --category
    calories INT CHECK (calories > 0) --calories of product must be >0
);
CREATE TABLE "consumption"
(
    id       SERIAL PRIMARY KEY, --unique id
    user_id  INT REFERENCES "user"(id) ON DELETE CASCADE, /* connection with
table "user", when user deleted his consumptions deleted too */
    product_id INT REFERENCES "product"(id) ON DELETE CASCADE, /* connection
with table "product", when prod deleted its cons. del too */
    quantity INT CHECK (quantity > 0) --must be >0
)
