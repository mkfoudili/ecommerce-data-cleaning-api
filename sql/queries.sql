-- 01 : Get all products with category names and prices
SELECT 
  g.`goods-id`,
  g.`goods-title`,
  c.category,
  g.price
FROM goods g
JOIN categories c ON g.`category-id`  = c.`category-id` ;

-- 02 : Get all categories
SELECT 
  `category-id` , 
  category 
FROM categories;

-- 03 : Get products in a specific category
SELECT 
  g.`goods-id`,
  g.`goods-title`,
  g.price
FROM goods g
JOIN categories c ON g.`category-id`  = c.`category-id` 
WHERE c.category = 'Tools And Home Improvement';

-- 04 : Add a new category
INSERT INTO categories (`category-id` , category) 
VALUES (3, 'Furniture');

-- 05 : Add a new product
INSERT INTO goods 
  (`goods-id`, `goods-title`, price, discount, `color-count`, `rank-title`, `rank-sub`, `selling-proposition`, `category-id`)
VALUES
  (89346, 'Office Chair', 89.99, 10, 3, 4, 'Comfortable ergonomic chair', 4000, 3);

-- 06 : Update the price of a product
UPDATE goods
SET price = 69.99
WHERE `goods-id` = 101;

-- 07 : Remove a product by its ID
DELETE FROM goods
WHERE `goods-id` = 105;

-- 08 : Query the view for a summarized list of all products with prices and categories
SELECT * FROM goods_summary;

-- 09 : Get the most expensive product in a certain category
SELECT 
  g.`goods-id`,
  g.`goods-title`,
  g.price,
  g.`rank-title`
FROM goods g
JOIN categories c ON g.`category-id` = c.`category-id`
WHERE c.category = 'Electronics'
ORDER BY g.price DESC
LIMIT 1;

-- 10 : SELECT: Get all products with a discount greater than 20%
SELECT 
  g.`goods-id`,
  g.`goods-title`,
  g.price,
  g.discount
FROM goods g
WHERE g.discount > 20
ORDER BY g.discount;

-- 11 : SELECT: Get the total number of products in each category
SELECT 
  c.category,
  COUNT(g.`goods-id`) AS product_count
FROM categories c
LEFT JOIN goods g ON c.`category-id` = g.`category-id`
GROUP BY c.category;