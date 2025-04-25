-- option : 03 : creating tables manually with sql

CREATE TABLE categories (
  `category-id` BIGINT PRIMARY KEY,
  category TEXT
);

CREATE TABLE goods (
  `goods-id` BIGINT PRIMARY KEY,
  `goods-title` TEXT,
  price DOUBLE,
  discount BIGINT,
  `color-count` DOUBLE,
  `rank-title` BIGINT,
  `rank-sub` TEXT,
  `selling-proposition` DOUBLE,
  `category-id` BIGINT,
  FOREIGN KEY (`category-id`) REFERENCES categories(`category-id`)
);