/*
Navicat MySQL Data Transfer

Source Server         : vic
Source Server Version : 50547
Source Host           : localhost:3306
Source Database       : vuldb

Target Server Type    : MYSQL
Target Server Version : 50547
File Encoding         : 65001

Date: 2017-04-01 18:49:37
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for cnvdvul_copy
-- ----------------------------
DROP TABLE IF EXISTS `cnvdvul_copy`;
CREATE TABLE `cnvdvul_copy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `CNVD_ID` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `level` varchar(255) NOT NULL,
  `url` text NOT NULL,
  `archdate` varchar(255) NOT NULL,
  `cause` varchar(255) DEFAULT NULL,
  `harm` varchar(255) DEFAULT NULL,
  `attway` varchar(255) DEFAULT NULL,
  `vultype` varchar(255) DEFAULT NULL,
  `effect_production` varchar(255) DEFAULT NULL,
  `hot` varchar(255) DEFAULT NULL,
  `company` varchar(255) DEFAULT NULL,
  `cve_id` varchar(255) DEFAULT NULL,
  `cve_url` text,
  `bugtraq_id` varchar(255) DEFAULT NULL,
  `bugtraq_url` text,
  `vul_detial` varchar(255) DEFAULT NULL,
  `look_link` varchar(255) DEFAULT NULL,
  `patch` varchar(255) DEFAULT NULL,
  `patchdetial` varchar(255) DEFAULT NULL,
  `patchlink` varchar(255) DEFAULT NULL,
  `solution` varchar(255) DEFAULT NULL,
  `solution_url` text,
  `entdate` varchar(255) DEFAULT NULL,
  `subdate` varchar(255) DEFAULT NULL,
  `pubdate` varchar(255) DEFAULT NULL,
  `discdate` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;
