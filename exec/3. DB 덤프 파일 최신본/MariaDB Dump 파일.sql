-- --------------------------------------------------------
-- 호스트:                          i9e101.p.ssafy.io
-- 서버 버전:                        10.11.4-MariaDB-1:10.11.4+maria~ubu2204 - mariadb.org binary distribution
-- 서버 OS:                        debian-linux-gnu
-- HeidiSQL 버전:                  12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- mlm 데이터베이스 구조 내보내기
DROP DATABASE IF EXISTS `mlm`;
CREATE DATABASE IF NOT EXISTS `mlm` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `mlm`;

-- 테이블 mlm.connect_users 구조 내보내기
DROP TABLE IF EXISTS `connect_users`;
CREATE TABLE IF NOT EXISTS `connect_users` (
  `user_id` bigint(20) NOT NULL,
  `connect_user_id` bigint(20) NOT NULL,
  `connect_user_alias` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`connect_user_id`,`user_id`),
  KEY `connect_user_from_user_user_id_fk` (`user_id`),
  CONSTRAINT `connect_user_from_user_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `connect_user_from_user_user_id_fk2` FOREIGN KEY (`connect_user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 테이블 데이터 mlm.connect_users:~28 rows (대략적) 내보내기
DELETE FROM `connect_users`;
INSERT INTO `connect_users` (`user_id`, `connect_user_id`, `connect_user_alias`) VALUES
	(5, 2, '사촌동생'),
	(9, 2, '귤'),
	(10, 2, '김규리'),
	(11, 2, '조카'),
	(12, 2, '김규리'),
	(13, 2, '김규리'),
	(2, 5, '주원언니'),
	(10, 5, '아는 여동생'),
	(11, 5, '울딸'),
	(2, 9, '너구리'),
	(10, 9, '너구리'),
	(12, 9, '너구리'),
	(13, 9, '너규리'),
	(2, 10, '이진형'),
	(5, 10, '아는 오빠'),
	(9, 10, '찐'),
	(12, 10, '이진형'),
	(13, 10, '이진형'),
	(2, 11, '삼촌'),
	(5, 11, '아빠'),
	(2, 12, '김성현'),
	(9, 12, '썽'),
	(10, 12, '김성현'),
	(13, 12, '김성현'),
	(2, 13, '이소정'),
	(9, 13, '이소정'),
	(10, 13, '이소정'),
	(12, 13, '이소정');

-- 테이블 mlm.emotion 구조 내보내기
DROP TABLE IF EXISTS `emotion`;
CREATE TABLE IF NOT EXISTS `emotion` (
  `emotion_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `create_at` datetime(6) DEFAULT NULL,
  `emotion_code` int(11) NOT NULL,
  `emotion_date` date DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`emotion_id`),
  KEY `emotion_from_user_user_id_fk` (`user_id`),
  KEY `emotion_from_emotion_code_fk` (`emotion_code`),
  CONSTRAINT `emotion_from_emotion_code_fk` FOREIGN KEY (`emotion_code`) REFERENCES `emotion_code` (`emotion_code`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `emotion_from_user_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 테이블 데이터 mlm.emotion:~14 rows (대략적) 내보내기
DELETE FROM `emotion`;
INSERT INTO `emotion` (`emotion_id`, `create_at`, `emotion_code`, `emotion_date`, `user_id`) VALUES
	(6, '2023-08-09 15:48:41.390597', 1, '2023-08-08', 2),
	(8, '2023-08-09 16:59:49.730013', 1, '2023-08-06', 2),
	(9, '2023-08-11 16:59:49.730000', 4, '2023-08-12', 5),
	(10, '2023-08-11 20:59:49.730000', 3, '2023-08-12', 10),
	(15, '2023-08-14 17:44:49.636380', 2, '2023-08-14', 2),
	(17, '2023-08-14 23:11:51.377415', 2, '2023-08-14', 5),
	(18, '2023-08-14 23:33:49.633364', 2, '2023-08-14', 9),
	(22, '2023-08-15 00:03:49.428346', 2, '2023-08-15', 11),
	(26, '2023-08-15 11:26:16.806984', 3, '2023-08-15', 11),
	(27, '2023-08-15 11:26:30.863366', 3, '2023-08-15', 11),
	(28, '2023-08-15 11:26:39.750779', 3, '2023-08-15', 11),
	(29, '2023-08-15 11:26:48.851437', 3, '2023-08-15', 11),
	(33, '2023-08-15 11:57:36.242635', 4, '2023-08-15', 11),
	(34, '2023-08-15 17:10:17.442524', 2, '2023-08-15', 5);

-- 테이블 mlm.emotion_code 구조 내보내기
DROP TABLE IF EXISTS `emotion_code`;
CREATE TABLE IF NOT EXISTS `emotion_code` (
  `emotion_code` int(11) NOT NULL,
  `emotion_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`emotion_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 테이블 데이터 mlm.emotion_code:~5 rows (대략적) 내보내기
DELETE FROM `emotion_code`;
INSERT INTO `emotion_code` (`emotion_code`, `emotion_name`) VALUES
	(0, 'NULL'),
	(1, 'happy'),
	(2, 'neutral'),
	(3, 'sad'),
	(4, 'angry');

-- 테이블 mlm.emotion_count 구조 내보내기
DROP TABLE IF EXISTS `emotion_count`;
CREATE TABLE IF NOT EXISTS `emotion_count` (
  `emotion_code` int(11) NOT NULL,
  `emotion_id` bigint(20) NOT NULL,
  `emotion_count` int(11) NOT NULL,
  PRIMARY KEY (`emotion_code`,`emotion_id`),
  KEY `emotion_count_from_emotion_cmotion_id` (`emotion_id`),
  CONSTRAINT `emotion_count_from_emotion_cmotion_id` FOREIGN KEY (`emotion_id`) REFERENCES `emotion` (`emotion_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `emotion_count_from_emotion_code_code_fk` FOREIGN KEY (`emotion_code`) REFERENCES `emotion_code` (`emotion_code`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 테이블 데이터 mlm.emotion_count:~34 rows (대략적) 내보내기
DELETE FROM `emotion_count`;
INSERT INTO `emotion_count` (`emotion_code`, `emotion_id`, `emotion_count`) VALUES
	(1, 6, 5),
	(1, 15, 2),
	(1, 17, 22),
	(1, 18, 1),
	(1, 34, 143),
	(2, 8, 3),
	(2, 15, 46),
	(2, 17, 26),
	(2, 18, 2),
	(2, 22, 17),
	(2, 34, 579),
	(3, 6, 1),
	(3, 8, 5),
	(3, 15, 26),
	(3, 17, 22),
	(3, 18, 1),
	(3, 22, 6),
	(3, 26, 27),
	(3, 27, 30),
	(3, 28, 29),
	(3, 29, 26),
	(3, 33, 6),
	(3, 34, 418),
	(4, 6, 2),
	(4, 8, 2),
	(4, 15, 7),
	(4, 17, 7),
	(4, 18, 2),
	(4, 22, 6),
	(4, 26, 2),
	(4, 28, 1),
	(4, 29, 4),
	(4, 33, 24),
	(4, 34, 184);

-- 테이블 mlm.households 구조 내보내기
DROP TABLE IF EXISTS `households`;
CREATE TABLE IF NOT EXISTS `households` (
  `household_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `create_user_id` bigint(20) DEFAULT NULL,
  `household_name` varchar(255) DEFAULT NULL,
  `grid_nx` bigint(20) DEFAULT NULL,
  `grid_ny` bigint(20) DEFAULT NULL,
  `region` varchar(255) DEFAULT NULL,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  PRIMARY KEY (`household_id`),
  KEY `households_from_user_user_id_fk` (`create_user_id`),
  CONSTRAINT `households_from_user_user_id_fk` FOREIGN KEY (`create_user_id`) REFERENCES `users` (`user_id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 테이블 데이터 mlm.households:~3 rows (대략적) 내보내기
DELETE FROM `households`;
INSERT INTO `households` (`household_id`, `create_user_id`, `household_name`, `grid_nx`, `grid_ny`, `region`, `latitude`, `longitude`) VALUES
	(1, 11, '아빠네', 96, 76, '부산광역시 강서구 신호동', NULL, NULL),
	(2, 5, '딸네', 61, 126, '서울특별시 강남구 역삼동', NULL, NULL),
	(3, 9, '친척집', 67, 100, '유성구', NULL, NULL);

-- 테이블 mlm.interests 구조 내보내기
DROP TABLE IF EXISTS `interests`;
CREATE TABLE IF NOT EXISTS `interests` (
  `interest_code` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `is_used` int(11) NOT NULL,
  PRIMARY KEY (`interest_code`,`user_id`),
  KEY `interest_from_users_user_id_fk` (`user_id`),
  CONSTRAINT `ineterest_from_interest_code_code_fk` FOREIGN KEY (`interest_code`) REFERENCES `interest_common_code` (`interest_code`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `interest_from_users_user_id_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 테이블 데이터 mlm.interests:~4 rows (대략적) 내보내기
DELETE FROM `interests`;
INSERT INTO `interests` (`interest_code`, `user_id`, `is_used`) VALUES
	(1, 2, 1),
	(2, 2, 1),
	(3, 13, 1),
	(5, 13, 1);

-- 테이블 mlm.interest_common_code 구조 내보내기
DROP TABLE IF EXISTS `interest_common_code`;
CREATE TABLE IF NOT EXISTS `interest_common_code` (
  `interest_code` bigint(20) NOT NULL,
  `interest_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`interest_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 테이블 데이터 mlm.interest_common_code:~7 rows (대략적) 내보내기
DELETE FROM `interest_common_code`;
INSERT INTO `interest_common_code` (`interest_code`, `interest_name`) VALUES
	(1, '가족'),
	(2, '회사'),
	(3, '건강'),
	(4, '정치'),
	(5, '경제'),
	(6, '생활'),
	(7, 'IT'),
	(8, '스포츠');

-- 테이블 mlm.mirrors 구조 내보내기
DROP TABLE IF EXISTS `mirrors`;
CREATE TABLE IF NOT EXISTS `mirrors` (
  `mirror_id` varchar(255) NOT NULL,
  `mirror_group_id` bigint(20) DEFAULT NULL,
  `mirror_place_code` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`mirror_id`),
  KEY `mirror_group_id_from_households_id_fk` (`mirror_group_id`),
  KEY `mirror_from_mirror_place_common_code_fk` (`mirror_place_code`),
  CONSTRAINT `mirror_from_mirror_place_common_code_fk` FOREIGN KEY (`mirror_place_code`) REFERENCES `mirror_place_common_code` (`mirror_place_code`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `mirror_group_id_from_households_id_fk` FOREIGN KEY (`mirror_group_id`) REFERENCES `households` (`household_id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 테이블 데이터 mlm.mirrors:~3 rows (대략적) 내보내기
DELETE FROM `mirrors`;
INSERT INTO `mirrors` (`mirror_id`, `mirror_group_id`, `mirror_place_code`) VALUES
	('2Z9jbhAnGf7LawDiThJW', 2, 1),
	('6rBZ68bBiJ46ntHGBfJP', 1, 2),
	('ReTySuGWJIMZU9EpiRuc', 3, 1);

-- 테이블 mlm.mirror_place_common_code 구조 내보내기
DROP TABLE IF EXISTS `mirror_place_common_code`;
CREATE TABLE IF NOT EXISTS `mirror_place_common_code` (
  `mirror_place_code` bigint(20) NOT NULL,
  `mirror_place_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`mirror_place_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 테이블 데이터 mlm.mirror_place_common_code:~2 rows (대략적) 내보내기
DELETE FROM `mirror_place_common_code`;
INSERT INTO `mirror_place_common_code` (`mirror_place_code`, `mirror_place_name`) VALUES
	(1, '현관'),
	(2, '거실'),
	(3, '개인방');

-- 테이블 mlm.users 구조 내보내기
DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `user_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `create_at` datetime(6) DEFAULT NULL,
  `household_id` bigint(20) DEFAULT NULL,
  `modified_at` datetime(6) DEFAULT NULL,
  `user_email` varchar(255) DEFAULT NULL,
  `user_name` varchar(255) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `birthday` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `users_from_household_id_fk` (`household_id`),
  CONSTRAINT `users_from_household_id_fk` FOREIGN KEY (`household_id`) REFERENCES `households` (`household_id`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 테이블 데이터 mlm.users:~7 rows (대략적) 내보내기
DELETE FROM `users`;
INSERT INTO `users` (`user_id`, `create_at`, `household_id`, `modified_at`, `user_email`, `user_name`, `password`, `birthday`) VALUES
	(2, '2023-08-13 15:54:05.542979', 3, '2023-08-10 16:01:30.000000', 'kkrt7777@gmail.com', '김규리', '123456789', '0202'),
	(5, '2023-08-10 16:00:17.000000', 2, '2023-08-10 16:01:32.000000', 'woneee99@gmail.com', '황주원', '123456789', '0819'),
	(9, '2023-08-11 00:25:56.548520', 3, '2023-08-11 11:45:20.000000', 'mandarining0918@gmail.com', '너규리', '123456789', '0817'),
	(10, '2023-08-11 11:45:14.000000', 3, '2023-08-11 11:45:20.000000', 'wlsgud4084@gmail.com', '이진형', '123456789', '0326'),
	(11, '2023-08-11 11:45:13.000000', 1, '2023-08-11 11:45:18.000000', 'shw2ny@gmail.com', '신성환', '123456789', '0815'),
	(12, '2023-08-11 11:45:14.000000', 3, '2023-08-11 11:45:16.000000', 'sunghyunkim224@gmail.com', '김성현', '123456789', '0101'),
	(13, '2023-08-14 10:00:14.289980', 3, NULL, 'chadireoroonu@gmail.com', '이소정', NULL, NULL);

-- 테이블 mlm.video_message 구조 내보내기
DROP TABLE IF EXISTS `video_message`;
CREATE TABLE IF NOT EXISTS `video_message` (
  `video_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` datetime(6) DEFAULT NULL,
  `is_read` char(1) DEFAULT NULL,
  `send_user_email` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `user_email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`video_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 테이블 데이터 mlm.video_message:~2 rows (대략적) 내보내기
DELETE FROM `video_message`;
INSERT INTO `video_message` (`video_id`, `date`, `is_read`, `send_user_email`, `type`, `user_email`) VALUES
	(10, '2023-08-10 15:57:00.000326', 'Y', 'woneee99@gmail.com', 'v', 'kkrt7777@gmail.com'),
	(11, '2023-08-12 19:42:00.000633', 'Y', 'mandarining0918@gmail.com', 'v', 'kkrt7777@gmail.com');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
