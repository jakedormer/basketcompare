SELECT bc_sku, product_type, product_description, product_price FROM products_product 
WHERE bc_sku IN ( 
SELECT DISTINCT bc_sku FROM 
products_project a 
INNER JOIN 
products_project_item b ON a.id = b.project_id 
INNER JOIN 
products_project_item_item c ON b.id = c.project_item_id 
INNER JOIN 
products_product d ON d.id = c.product_id 
WHERE project_slug = 'jakes-lawn' and user_id = 'jake') AND ( merchant_id IN (SELECT DISTINCT merchant_id FROM 
products_project a 
INNER JOIN 
products_project_item b ON a.id = b.project_id 
INNER JOIN 
products_project_merchants c on a.id = c.project_id 
WHERE project_slug = 'jakes-lawn' and user_id = 'jake') OR merchant_id = 'basket compare' ) 
ORDER BY bc_sku, product_type DESC