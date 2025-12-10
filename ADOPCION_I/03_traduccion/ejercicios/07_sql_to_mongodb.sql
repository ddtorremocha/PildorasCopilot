-- Ejercicio 7: SQL → MongoDB Aggregation
-- Convierte estas queries SQL a MongoDB aggregation pipeline

-- Query 1: Obtener productos con sus categorías
SELECT 
    p.id,
    p.name,
    p.price,
    c.name AS category_name
FROM products p
INNER JOIN categories c ON p.category_id = c.id
WHERE p.active = true
ORDER BY p.price DESC;

-- Query 2: Ventas totales por producto
SELECT 
    p.id,
    p.name,
    COUNT(oi.id) AS order_count,
    SUM(oi.quantity) AS total_sold,
    SUM(oi.quantity * oi.price) AS total_revenue
FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id
GROUP BY p.id, p.name
HAVING SUM(oi.quantity * oi.price) > 1000
ORDER BY total_revenue DESC
LIMIT 10;

-- Query 3: Usuarios con sus órdenes y total gastado
SELECT 
    u.id,
    u.name,
    u.email,
    COUNT(DISTINCT o.id) AS order_count,
    SUM(oi.quantity * oi.price) AS total_spent,
    AVG(oi.quantity * oi.price) AS avg_order_value
FROM users u
INNER JOIN orders o ON u.id = o.user_id
INNER JOIN order_items oi ON o.id = oi.order_id
WHERE o.status = 'completed'
  AND o.created_at >= DATE_SUB(NOW(), INTERVAL 1 YEAR)
GROUP BY u.id, u.name, u.email
HAVING COUNT(DISTINCT o.id) >= 5
ORDER BY total_spent DESC;

-- Query 4: Productos más vendidos por categoría
SELECT 
    c.name AS category,
    p.name AS product_name,
    SUM(oi.quantity) AS total_sold,
    RANK() OVER (PARTITION BY c.id ORDER BY SUM(oi.quantity) DESC) AS rank_in_category
FROM categories c
INNER JOIN products p ON c.id = p.category_id
INNER JOIN order_items oi ON p.id = oi.product_id
INNER JOIN orders o ON oi.order_id = o.id
WHERE o.status = 'completed'
GROUP BY c.id, c.name, p.id, p.name
HAVING rank_in_category <= 3;

-- Query 5: Análisis de tendencias mensuales
SELECT 
    DATE_FORMAT(o.created_at, '%Y-%m') AS month,
    COUNT(DISTINCT o.id) AS order_count,
    COUNT(DISTINCT o.user_id) AS unique_customers,
    SUM(oi.quantity * oi.price) AS revenue,
    AVG(oi.quantity * oi.price) AS avg_order_value
FROM orders o
INNER JOIN order_items oi ON o.id = oi.order_id
WHERE o.status = 'completed'
  AND o.created_at >= DATE_SUB(NOW(), INTERVAL 12 MONTH)
GROUP BY DATE_FORMAT(o.created_at, '%Y-%m')
ORDER BY month DESC;

-- Query 6: Clientes inactivos (sin compras recientes)
SELECT 
    u.id,
    u.name,
    u.email,
    MAX(o.created_at) AS last_order_date,
    DATEDIFF(NOW(), MAX(o.created_at)) AS days_since_last_order,
    COUNT(o.id) AS total_orders
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name, u.email
HAVING days_since_last_order > 90 OR days_since_last_order IS NULL
ORDER BY days_since_last_order DESC;
