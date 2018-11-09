SELECT DISTINCT t1.bc_sku,
				t1.product_description,
                quantity, 
                merchant_id, 
                Min(product_price), 
                product_price * quantity AS sub_total 
FROM   (SELECT * 
        FROM   products_product) t1 
       INNER JOIN (SELECT DISTINCT bc_sku, 
                                   quantity 
                   FROM   products_project a 
                          INNER JOIN products_project_item b 
                                  ON a.id = b.project_id 
                          INNER JOIN products_project_item_item c 
                                  ON b.id = c.project_item_id 
                          INNER JOIN products_product d 
                                  ON d.id = c.product_id 
                   WHERE  project_slug = 'hi' 
                          AND user_id = 'jake') t2 
               ON t1.bc_sku = t2.bc_sku 
WHERE  merchant_id = 'basket compare' 
        OR merchant_id IN (SELECT DISTINCT merchant_id 
                           FROM   products_project a 
                                  INNER JOIN products_project_item b 
                                          ON a.id = b.project_id 
                                  INNER JOIN products_project_merchants c 
                                          ON a.id = c.project_id 
                           WHERE  project_slug = 'hi' 
                                  AND user_id = 'jake') 
GROUP  BY merchant_id, 
          t1.bc_sku 
ORDER  BY t1.bc_sku, 
          product_price 