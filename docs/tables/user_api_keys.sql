CREATE TABLE `user_api_keys` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `user_id` integer,
  `exchange` varchar(255),
  `api_key` varchar(255),
  `secret_key` varchar(255)
);
