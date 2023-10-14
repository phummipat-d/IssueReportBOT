-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 14, 2023 at 01:43 PM
-- Server version: 5.6.35-log
-- PHP Version: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `issuereport`
--

-- --------------------------------------------------------

--
-- Table structure for table `appeal_info`
--

DROP TABLE IF EXISTS `appeal_info`;
CREATE TABLE `appeal_info` (
  `id` int(11) NOT NULL,
  `userId` varchar(200) DEFAULT NULL,
  `displayName` varchar(200) DEFAULT NULL,
  `personName` varchar(100) DEFAULT NULL,
  `detail` text,
  `progress` varchar(100) DEFAULT NULL,
  `lon` float DEFAULT NULL,
  `lat` float DEFAULT NULL,
  `unit` varchar(200) DEFAULT NULL,
  `updateDate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `images`
--

DROP TABLE IF EXISTS `images`;
CREATE TABLE `images` (
  `id` int(11) NOT NULL,
  `message_id` varchar(200) DEFAULT NULL,
  `path` varchar(200) NOT NULL,
  `fid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `progress`
--

DROP TABLE IF EXISTS `progress`;
CREATE TABLE `progress` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `progress`
--

INSERT INTO `progress` (`id`, `name`) VALUES
(1, 'รอตรวจสอบ'),
(2, 'กำลังดำเนินการ'),
(3, 'เรียบร้อย');

-- --------------------------------------------------------

--
-- Table structure for table `unit`
--

DROP TABLE IF EXISTS `unit`;
CREATE TABLE `unit` (
  `id` int(11) NOT NULL,
  `Name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `unit`
--

INSERT INTO `unit` (`id`, `Name`) VALUES
(1, 'แผนกงานอาคาร'),
(2, 'แผนกงานไฟฟ้า'),
(3, 'แผนกงานประปา');

-- --------------------------------------------------------

--
-- Table structure for table `userlog`
--

DROP TABLE IF EXISTS `userlog`;
CREATE TABLE `userlog` (
  `ID` bigint(20) NOT NULL,
  `UserID` varchar(500) NOT NULL,
  `AccessTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `UserName` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `Password` varchar(100) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `FullName` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `Authority` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`UserName`, `Password`, `FullName`, `Authority`) VALUES
('admin', '21232f297a57a5a743894a0e4a801fc3', 'Administrator', 'Administrator');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appeal_info`
--
ALTER TABLE `appeal_info`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `images`
--
ALTER TABLE `images`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `progress`
--
ALTER TABLE `progress`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `unit`
--
ALTER TABLE `unit`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`UserName`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appeal_info`
--
ALTER TABLE `appeal_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `images`
--
ALTER TABLE `images`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `progress`
--
ALTER TABLE `progress`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `unit`
--
ALTER TABLE `unit`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
