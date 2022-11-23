/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - blood_bank
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`blood_bank` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `blood_bank`;

/*Table structure for table `bloodbank` */

DROP TABLE IF EXISTS `bloodbank`;

CREATE TABLE `bloodbank` (
  `bank_id` int(11) NOT NULL AUTO_INCREMENT,
  `hospital_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` varchar(50) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `bank_loginid` int(11) DEFAULT NULL,
  PRIMARY KEY (`bank_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `bloodbank` */

insert  into `bloodbank`(`bank_id`,`hospital_name`,`place`,`post`,`pin`,`phone`,`email`,`bank_loginid`) values 
(5,'malabar','calicut','Mavoor','673008',9847589657,'basil8592@gmail.com',11),
(6,'baby','calicut','calicut','673001',9823475393,'baby',12),
(8,'mims','calicut','calicut','673001',9823475393,'baby@gmail.com',8),
(9,'baby','calicut','calicut','673001',8592816001,'basil8592@gmail.com',20),
(10,'mvr','calicut','calicut','1234',9072485731,'admin@example.com',21),
(11,'shanti','omassery','calicut','23435',668748597486,'shanti@gmail.com',23),
(13,'al shifa','perunthalmanna','perunthalmanna','673661',9072485731,'al shifa@example.com',31);

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `cmp_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `complaint` varchar(50) DEFAULT NULL,
  `bank_loginid` int(11) NOT NULL,
  `reply` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cmp_id`,`bank_loginid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`cmp_id`,`date`,`complaint`,`bank_loginid`,`reply`) values 
(1,'2022-02-04','bloodbank is empty',8,'dfghjkl'),
(2,'2022-02-10','bloodbank is full',8,'pending'),
(3,'2022-03-03','polkijuhyggtfc',21,'bkn'),
(4,'2022-03-03','aman is always playing',21,'nhjghbhjk'),
(5,'2022-03-03','gu',21,'ghbjn'),
(6,'2022-03-03','not fast',21,'ok'),
(7,'2022-03-05','rgz',2,'pending'),
(8,'2022-03-14','sgdsbfg',21,'pending');

/*Table structure for table `donate` */

DROP TABLE IF EXISTS `donate`;

CREATE TABLE `donate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hlid` int(11) DEFAULT NULL,
  `ulid` int(11) DEFAULT NULL,
  `blood` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `count` int(11) DEFAULT NULL,
  `date` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `donate` */

insert  into `donate`(`id`,`hlid`,`ulid`,`blood`,`status`,`count`,`date`) values 
(1,13,30,'A+','donation',1,'2022-03-20');

/*Table structure for table `emergency_alert` */

DROP TABLE IF EXISTS `emergency_alert`;

CREATE TABLE `emergency_alert` (
  `emergency_id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `bloodgrp` varchar(50) DEFAULT NULL,
  `count` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`emergency_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

/*Data for the table `emergency_alert` */

insert  into `emergency_alert`(`emergency_id`,`lid`,`date`,`bloodgrp`,`count`,`status`) values 
(24,8,'2022-03-20','B+','4','approve'),
(25,23,'2022-03-20','AB+','73','approve'),
(26,23,'2022-03-20','B+','32','approve'),
(27,23,'2022-03-20','B+','5','approve'),
(28,31,'2022-03-20','A+','5','approve');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `bank_loginid` int(11) DEFAULT NULL,
  `feedback` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`date`,`bank_loginid`,`feedback`) values 
(1,'2022-02-26',8,'polikijjhsjgvgj'),
(2,'2022-02-27',2,'faxadfsc'),
(3,'2022-03-01',2,'hellow world'),
(4,'2022-03-01',2,'aman is bad'),
(7,'2022-03-03',21,'polkijmnhb'),
(8,'2022-03-03',21,'hjj'),
(9,'2022-03-03',21,'good'),
(10,'2022-03-03',2,'ghjk'),
(11,'2022-03-10',2,'hkj'),
(12,'2022-03-12',2,'police statiion'),
(13,'2022-03-12',2,'ggg'),
(14,'2022-03-17',2,''),
(15,'2022-03-20',30,'hi very good ');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(8,'mims','mims','bloodbank'),
(11,'malabar','malabar','bloodbank'),
(21,'mvr','mvr','bloodbank'),
(23,'shanti','shanti','bloodbank'),
(27,'sana','sana','user'),
(28,'firoz','firoz','user'),
(29,'fida','fida','user'),
(30,'shahid','shahid','user'),
(31,'alshifa','alshifa','bloodbank'),
(32,'hana','hana@123','user'),
(33,'finu','finu','blocked'),
(34,'faiz','faiiza','user'),
(35,'hafiz','hafiz@123','user');

/*Table structure for table `responce` */

DROP TABLE IF EXISTS `responce`;

CREATE TABLE `responce` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `ulid` int(11) DEFAULT NULL,
  `emergid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;

/*Data for the table `responce` */

insert  into `responce`(`rid`,`ulid`,`emergid`,`date`,`status`) values 
(29,27,24,'2022-03-20','accepted'),
(30,28,25,'2022-03-20','accepted'),
(31,29,26,'2022-03-20','accepted'),
(32,30,27,'2022-03-20','accepted'),
(33,28,28,'2022-03-20','accepted');

/*Table structure for table `stock` */

DROP TABLE IF EXISTS `stock`;

CREATE TABLE `stock` (
  `stock_id` int(11) NOT NULL AUTO_INCREMENT,
  `blood_bank_loginid` int(11) DEFAULT NULL,
  `blood_group` varchar(50) DEFAULT NULL,
  `stock` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`stock_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `stock` */

insert  into `stock`(`stock_id`,`blood_bank_loginid`,`blood_group`,`stock`) values 
(2,1,'o+','lljljk'),
(3,1,'A+','900'),
(10,2,'A+','5'),
(11,21,'o+','9'),
(12,2,'select',''),
(13,23,'o+','10'),
(14,23,'o-','6'),
(15,23,'A+','15'),
(16,23,'A-','7'),
(17,23,'B+','24'),
(18,23,'B-','13'),
(19,23,'AB+','7'),
(20,23,'AB-','14'),
(21,21,'o-','4');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `userlid` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `blood_group` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`userlid`,`fname`,`lname`,`blood_group`,`place`,`post`,`pin`,`phone`,`email`) values 

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
