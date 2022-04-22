CREATE TABLE `invite_codes` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `code` varchar(255),
  `user_id` integer
);