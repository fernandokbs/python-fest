CREATE TABLE `visit` (
  `id` int NOT NULL AUTO_INCREMENT,
  `timestamp` datetime DEFAULT (now()),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;