-- RETAIL SUPPLY CHAIN INTELLIGENCE
-- BUSINESS ANALYSIS


-- 1. What is the overall business performance?

SELECT
    SUM(oi.qty * oi.price) AS total_revenue,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(DISTINCT o.customer_id) AS total_customers,
    SUM(oi.qty) AS total_units_sold
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id;


-- 2. What is the average order value?

SELECT
    ROUND(
        SUM(oi.qty * oi.price) / COUNT(DISTINCT o.order_id),
        2
    ) AS average_order_value
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id;


-- 3. How does revenue and order volume change over time?

SELECT
    DATE_TRUNC('month', o.order_date) AS month,
    SUM(oi.qty * oi.price) AS revenue,
    COUNT(DISTINCT o.order_id) AS orders
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY month
ORDER BY month;


-- 4. Which months generate the highest revenue?

SELECT
    DATE_TRUNC('month', o.order_date) AS month,
    SUM(oi.qty * oi.price) AS revenue
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY month
ORDER BY revenue DESC;


-- 5. Which products generate the most revenue?

SELECT
    p.product_id,
    p.category_id,
    SUM(oi.qty * oi.price) AS revenue,
    SUM(oi.qty) AS units_sold
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY
    p.product_id,
    p.category_id
ORDER BY revenue DESC
LIMIT 10;


-- 6. Which products sell the most units?

SELECT
    p.product_id,
    p.category_id,
    SUM(oi.qty) AS units_sold,
    SUM(oi.qty * oi.price) AS revenue
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY
    p.product_id,
    p.category_id
ORDER BY units_sold DESC
LIMIT 10;


-- 7. Which product categories generate the most revenue?

SELECT
    c.category_id,
    c.category_name,
    SUM(oi.qty * oi.price) AS revenue,
    SUM(oi.qty) AS units_sold
FROM categories c
JOIN products p
    ON c.category_id = p.category_id
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY
    c.category_id,
    c.category_name
ORDER BY revenue DESC;


-- 8. Which stores generate the most revenue and orders?

SELECT
    s.store_id,
    s.city,
    SUM(oi.qty * oi.price) AS revenue,
    COUNT(DISTINCT o.order_id) AS orders,
    SUM(oi.qty) AS units_sold
FROM stores s
JOIN orders o
    ON s.store_id = o.store_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY
    s.store_id,
    s.city
ORDER BY revenue DESC;


-- 9. How does average order value vary across stores?

SELECT
    s.store_id,
    s.city,
    ROUND(
        SUM(oi.qty * oi.price) / COUNT(DISTINCT o.order_id),
        2
    ) AS average_order_value
FROM stores s
JOIN orders o
    ON s.store_id = o.store_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY
    s.store_id,
    s.city
ORDER BY average_order_value DESC;


-- 10. Which customers generate the most revenue?

SELECT
    c.customer_id,
    c.city,
    COUNT(DISTINCT o.order_id) AS orders,
    SUM(oi.qty * oi.price) AS revenue
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY
    c.customer_id,
    c.city
ORDER BY revenue DESC
LIMIT 20;


-- 11. How is revenue distributed across customers?

SELECT
    COUNT(*) AS customers,
    SUM(customer_revenue) AS revenue
FROM (
    SELECT
        o.customer_id,
        SUM(oi.qty * oi.price) AS customer_revenue
    FROM orders o
    JOIN order_items oi
        ON o.order_id = oi.order_id
    GROUP BY o.customer_id
) customer_sales;


-- 12. Which suppliers contribute the most revenue?

SELECT
    s.supplier_id,
    s.country,
    SUM(oi.qty * oi.price) AS revenue,
    SUM(oi.qty) AS units_sold
FROM suppliers s
JOIN products p
    ON s.supplier_id = p.supplier_id
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY
    s.supplier_id,
    s.country
ORDER BY revenue DESC
LIMIT 20;


-- 13. What is the distribution of shipment statuses?

SELECT
    status,
    COUNT(*) AS shipments,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (),
        2
    ) AS percentage
FROM shipments
GROUP BY status
ORDER BY shipments DESC;


-- 14. Which stores have the most shipments by status?

SELECT
    o.store_id,
    s.city,
    sh.status,
    COUNT(*) AS shipments
FROM shipments sh
JOIN orders o
    ON sh.order_id = o.order_id
JOIN stores s
    ON o.store_id = s.store_id
GROUP BY
    o.store_id,
    s.city,
    sh.status
ORDER BY
    o.store_id,
    shipments DESC;


-- 15. What is the overall return rate and total refunded amount?

SELECT
    COUNT(DISTINCT r.return_id) AS total_returns,
    COUNT(DISTINCT r.order_item_id) AS returned_order_items,
    ROUND(
        COUNT(DISTINCT r.order_item_id) * 100.0
        / COUNT(DISTINCT oi.order_item_id),
        2
    ) AS return_rate_percentage,
    SUM(r.refund) AS total_refunded_amount
FROM returns r
CROSS JOIN order_items oi;


-- 16. Which products have the most returns?

SELECT
    p.product_id,
    p.category_id,
    COUNT(r.return_id) AS returns,
    SUM(r.refund) AS refunded_amount
FROM returns r
JOIN order_items oi
    ON r.order_item_id = oi.order_item_id
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY
    p.product_id,
    p.category_id
ORDER BY returns DESC
LIMIT 20;


-- 17. Which categories have the most returns?

SELECT
    c.category_id,
    c.category_name,
    COUNT(r.return_id) AS returns,
    SUM(r.refund) AS refunded_amount
FROM returns r
JOIN order_items oi
    ON r.order_item_id = oi.order_item_id
JOIN products p
    ON oi.product_id = p.product_id
JOIN categories c
    ON p.category_id = c.category_id
GROUP BY
    c.category_id,
    c.category_name
ORDER BY returns DESC;


-- 18. How do promoted and non-promoted orders compare?

SELECT
    CASE
        WHEN o.promotion_id IS NULL THEN 'No Promotion'
        ELSE 'Promotion'
    END AS order_type,
    COUNT(DISTINCT o.order_id) AS orders,
    SUM(oi.qty) AS units_sold,
    SUM(oi.qty * oi.price) AS revenue,
    ROUND(
        SUM(oi.qty * oi.price)
        / COUNT(DISTINCT o.order_id),
        2
    ) AS average_order_value
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY order_type
ORDER BY revenue DESC;


-- 19. Which promotions are associated with the highest sales?

SELECT
    p.promotion_id,
    p.discount,
    COUNT(DISTINCT o.order_id) AS orders,
    SUM(oi.qty) AS units_sold,
    SUM(oi.qty * oi.price) AS revenue
FROM promotions p
JOIN orders o
    ON p.promotion_id = o.promotion_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY
    p.promotion_id,
    p.discount
ORDER BY revenue DESC;


-- 20. Which stores generate the most revenue while also having
-- the highest number of returns?

SELECT
    s.store_id,
    s.city,
    SUM(oi.qty * oi.price) AS revenue,
    COUNT(DISTINCT r.return_id) AS returns
FROM stores s
JOIN orders o
    ON s.store_id = o.store_id
JOIN order_items oi
    ON o.order_id = oi.order_id
LEFT JOIN returns r
    ON oi.order_item_id = r.order_item_id
GROUP BY
    s.store_id,
    s.city
ORDER BY revenue DESC;