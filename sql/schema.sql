-- option : 03 : creating tables manually with sql

CREATE TABLE categories (
  `category-id` BIGINT PRIMARY KEY COMMENT 'Unique identifier for each product category',
  category TEXT VARCHAR(100) NOT NULL COMMENT 'Name of the product category'
) COMMENT = 'Contains high-level product categories';

CREATE TABLE goods (
  `goods-id` BIGINT PRIMARY KEY COMMENT 'Unique identifier for each product',
  `goods-title` TEXT COMMENT 'Name of the product',
  price DOUBLE COMMENT 'Base price of the product in $',
  discount BIGINT DEFAULT 0 COMMENT 'Discount percentage on the product (0-100)',
  `color-count` DOUBLE DEFAULT 0 COMMENT 'Number of color variations available',
  `rank-title` BIGINT DEFAULT 0 COMMENT 'Primary ranking score of the product Best Seller (0-10)',
  `rank-sub` TEXT COMMENT 'Description of the ranking category',
  `selling-proposition` DOUBLE COMMENT 'Amount recently sold',
  `category-id` BIGINT,
  FOREIGN KEY (`category-id`) REFERENCES categories(`category-id`)
)  COMMENT = 'Stores individual products along with pricing, category, and marketing info';

CREATE VIEW goods_with_category AS
SELECT 
  g.`goods-id`,
  g.`goods-title`,
  g.price,
  g.discount,
  g.`color-count`,
  g.`rank-title`,
  g.`rank-sub`,
  g.`selling-proposition`,
  c.category
FROM goods g
JOIN categories c ON g.`category-id` = c.`category-id`;

CREATE VIEW goods_summary AS
SELECT
  g.`goods-id`,
  g.`goods-title`,
  c.category,
  g.price
FROM goods g
JOIN categories c ON g.`category-id` = c.`category-id`;

CREATE INDEX idx_price ON goods(price);