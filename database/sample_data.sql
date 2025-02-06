INSERT INTO suppliers (name, contact_info, product_categories_offered)
VALUES 
    ('Supplier A', 'contact@supplierA.com', ARRAY['Electronics', 'Laptops']),
    ('Supplier B', 'contact@supplierB.com', ARRAY['Accessories', 'Smartphones']);

INSERT INTO products (name, brand, price, category, description, supplier_id)
VALUES 
    ('Laptop X1', 'Brand X', 1200.00, 'Laptops', 'High-performance laptop', 1),
    ('Smartphone Y1', 'Brand Y', 800.00, 'Smartphones', 'Latest smartphone model', 2),
     ('Laptop X2', 'Brand X2', 1200.00, 'Laptops', 'High-performance laptop', 3),
      ('Laptop X1', 'Brand X3', 1230.00, 'Laptops', 'High-performance laptop', 4),
       ('Laptop X1', 'Brand X4', 1400.00, 'Laptops', 'High-performance laptop', 5),
        ('Laptop X1', 'Brand X5', 1600.00, 'Laptops', 'High-performance laptop', 6),
         ('Laptop X1', 'Brand X6', 1800.00, 'Laptops', 'High-performance laptop', 7);