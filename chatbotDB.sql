create database Chatbot;
use Chatbot;

CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact_info TEXT,
    product_categories TEXT
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    brand VARCHAR(255),
    price DECIMAL(10,2),
    category VARCHAR(100),
    description TEXT,
    supplier_id INT REFERENCES suppliers(id) ON DELETE CASCADE
);
