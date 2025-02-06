CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_info TEXT,
    categories TEXT
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    brand VARCHAR(255),
    price DECIMAL(10,2),
    category VARCHAR(255),
    description TEXT,
    supplier_id INT REFERENCES suppliers(id)
);