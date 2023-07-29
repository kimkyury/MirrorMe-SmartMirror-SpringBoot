-- MariaDB dump 10.19  Distrib 10.11.4-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: mlm
-- ------------------------------------------------------
-- Server version	10.11.4-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `connect_members`
--

DROP TABLE IF EXISTS `connect_members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `connect_members` (
  `user_id` bigint(20) NOT NULL,
  `connect_member_id` bigint(20) NOT NULL,
  `connect_member_alias` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`,`connect_member_id`) USING BTREE,
  KEY `connect_members_from_users_user_id_to_connect_members_id_fk` (`connect_member_id`) USING BTREE,
  CONSTRAINT `connect_members_from_users_user_id_to_connect_member_id_fk` FOREIGN KEY (`connect_member_id`) REFERENCES `users` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `connect_members_from_users_user_id_to_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `connect_members`
--

LOCK TABLES `connect_members` WRITE;
/*!40000 ALTER TABLE `connect_members` DISABLE KEYS */;
INSERT INTO `connect_members` VALUES
(1,2,'주원언니'),
(1,3,'팀장님'),
(1,4,'소정언니'),
(1,7,'엄마'),
(2,3,'팀장님');
/*!40000 ALTER TABLE `connect_members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `households`
--

DROP TABLE IF EXISTS `households`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `households` (
  `household_id` bigint(20) NOT NULL,
  `household_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`household_id`),
  CONSTRAINT `households_from_mirror_groups_mirror_group_id_fk` FOREIGN KEY (`household_id`) REFERENCES `mirror_groups` (`mirror_group_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `households`
--

LOCK TABLES `households` WRITE;
/*!40000 ALTER TABLE `households` DISABLE KEYS */;
INSERT INTO `households` VALUES
(1,'우리집'),
(2,'우리집');
/*!40000 ALTER TABLE `households` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `interest_common_code`
--

DROP TABLE IF EXISTS `interest_common_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `interest_common_code` (
  `interest_code` bigint(20) NOT NULL,
  `interest_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`interest_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interest_common_code`
--

LOCK TABLES `interest_common_code` WRITE;
/*!40000 ALTER TABLE `interest_common_code` DISABLE KEYS */;
INSERT INTO `interest_common_code` VALUES
(1,'Family'),
(2,'Business'),
(3,'Health'),
(4,'Politics'),
(5,'Economy'),
(6,'Life'),
(7,'IT'),
(8,'Sports');
/*!40000 ALTER TABLE `interest_common_code` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `interests`
--

DROP TABLE IF EXISTS `interests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `interests` (
  `user_id` bigint(20) NOT NULL,
  `interest_code` bigint(20) NOT NULL,
  `is_used` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`user_id`,`interest_code`),
  KEY `intrerests_from_interests_common_code_interest_code_fk` (`interest_code`),
  CONSTRAINT `interests_from_users_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `intrerests_from_interests_common_code_interest_code_fk` FOREIGN KEY (`interest_code`) REFERENCES `interest_common_code` (`interest_code`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interests`
--

LOCK TABLES `interests` WRITE;
/*!40000 ALTER TABLE `interests` DISABLE KEYS */;
INSERT INTO `interests` VALUES
(1,1,1),
(2,2,1);
/*!40000 ALTER TABLE `interests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mirror_groups`
--

DROP TABLE IF EXISTS `mirror_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mirror_groups` (
  `mirror_group_id` bigint(20) NOT NULL,
  PRIMARY KEY (`mirror_group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mirror_groups`
--

LOCK TABLES `mirror_groups` WRITE;
/*!40000 ALTER TABLE `mirror_groups` DISABLE KEYS */;
INSERT INTO `mirror_groups` VALUES
(1),
(2),
(3);
/*!40000 ALTER TABLE `mirror_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mirror_place_common_code`
--

DROP TABLE IF EXISTS `mirror_place_common_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mirror_place_common_code` (
  `mirror_place_code` bigint(20) NOT NULL,
  `mirror_place_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`mirror_place_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mirror_place_common_code`
--

LOCK TABLES `mirror_place_common_code` WRITE;
/*!40000 ALTER TABLE `mirror_place_common_code` DISABLE KEYS */;
INSERT INTO `mirror_place_common_code` VALUES
(1,'현관'),
(2,'거울');
/*!40000 ALTER TABLE `mirror_place_common_code` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mirrors`
--

DROP TABLE IF EXISTS `mirrors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mirrors` (
  `mirror_id` bigint(20) NOT NULL,
  `mirror_group_id` bigint(20) DEFAULT NULL,
  `mirror_place_code` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`mirror_id`),
  KEY `mirrors_from_mirror_groups_mirror_group_id_fk` (`mirror_group_id`),
  KEY `mirror_place_code_from_mirror_place_common_code_fk` (`mirror_place_code`),
  CONSTRAINT `mirror_place_code_from_mirror_place_common_code_fk` FOREIGN KEY (`mirror_place_code`) REFERENCES `mirror_place_common_code` (`mirror_place_code`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `mirrors_from_mirror_groups_mirror_group_id_fk` FOREIGN KEY (`mirror_group_id`) REFERENCES `mirror_groups` (`mirror_group_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mirrors`
--

LOCK TABLES `mirrors` WRITE;
/*!40000 ALTER TABLE `mirrors` DISABLE KEYS */;
INSERT INTO `mirrors` VALUES
(1,1,1),
(2,1,2),
(3,2,1),
(4,2,2);
/*!40000 ALTER TABLE `mirrors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `user_id` bigint(20) NOT NULL,
  `user_password` varchar(50) NOT NULL,
  `user_nickame` varchar(50) DEFAULT NULL,
  `user_email` varchar(50) DEFAULT NULL,
  `user_name` varchar(50) DEFAULT NULL,
  `profile_image_url` text DEFAULT NULL,
  `create_at` datetime DEFAULT NULL,
  `modified_at` datetime DEFAULT NULL,
  `household_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_email` (`user_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES
(1,'@qw1','귤','mandarining0918@gmail.com','김규리','C:Users\\SSAFY\\Desktop\\img\\puppy1.png','2023-07-22 15:49:57','2023-07-22 15:49:57',2),
(2,'@qw1','주원','kkrt7777@gmail.com','황주원','C:Users\\SSAFY\\Desktop\\img\\puppy2.png','2023-07-22 15:50:44','2023-07-22 15:50:44',1),
(3,'@qw1','성환','test7@gmail.com','신성환','C:Users\\SSAFY\\Desktop\\img\\puppy1.png','2023-07-22 21:23:06','2023-07-22 21:23:06',1),
(4,'@qw1','소정','test8@gmail.com','이소정','C:Users\\SSAFY\\Desktop\\img\\puppy3.png','2023-07-22 21:23:06','2023-07-22 21:23:06',1),
(5,'@qw1','성현','test5@gmail.com','김성현','C:Users\\SSAFY\\Desktop\\img\\puppy4.png','2023-07-22 21:23:06','2023-07-22 21:23:06',2),
(6,'@qw1','진형','test6@gmail.com','이진형','C:Users\\SSAFY\\Desktop\\img\\puppy1.png','2023-07-22 21:23:06','2023-07-22 21:23:06',2),
(7,'@qw1','김익명','test9@gmail.com','김익명','C:Users\\SSAFY\\Desktop\\img\\puppy1.png',NULL,NULL,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-25  9:33:32
