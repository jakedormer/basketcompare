SELECT t4.product_description, 
       t3.quantity, 
       t3.merchant, 
       t3.product_price, 
       t3.sub_total 
FROM   (SELECT DISTINCT t1.bc_sku, 
                        Sum(t2.quantity)                      AS Quantity, 
                        t1.merchant_id                        AS Merchant, 
                        Min(product_price)                    AS Product_Price, 
                        Min(product_price) * Sum(t2.quantity) AS Sub_Total 
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
                                          INNER JOIN products_project_merchants 
                                                     c 
                                                  ON a.id = c.project_id 
                                   WHERE  project_slug = 'hi' 
                                          AND user_id = 'jake') 
        GROUP  BY merchant_id, 
                  t1.bc_sku) t3 
       INNER JOIN (SELECT product_description, 
                          bc_sku 
                   FROM   products_product 
                   WHERE  product_type = 'master_product') t4 
               ON t3.bc_sku = t4.bc_sku 
WHERE  t3.merchant <> 'basket compare' 
ORDER  BY t4.product_description, 
          t3.merchant 