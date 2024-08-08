-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 30, 2022 at 12:37 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`) VALUES
('kanishka', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `bookid` varchar(50) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `author` varchar(50) DEFAULT NULL,
  `publisher` varchar(50) DEFAULT NULL,
  `copies` int(11) DEFAULT NULL,
  `avl` int(11) DEFAULT `copies`
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`bookid`, `name`, `author`, `publisher`, `copies`, `avl`) VALUES
('algo', 'introduction to algorithms', 'coremen', 'unknown', 4, 4),
('cnth', 'computer networks', 'Tanenbaum', 'unknown', 3, 2),
('pyre', 'python programming for beginnners', 'remma thereja', 'oxford', 4, 4);

-- --------------------------------------------------------

--
-- Table structure for table `book_details`
--

CREATE TABLE `book_details` (
  `bookid` varchar(50) DEFAULT NULL,
  `accno` int(11) DEFAULT NULL,
  `studentid` varchar(50) DEFAULT NULL,
  `doi` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `book_details`
--

INSERT INTO `book_details` (`bookid`, `accno`, `studentid`, `doi`) VALUES
('pyre', 1, NULL, NULL),
('pyre', 2, NULL, NULL),
('pyre', 3, NULL, NULL),
('pyre', 4, NULL, NULL),
('algo', 5, NULL, NULL),
('algo', 6, NULL, NULL),
('algo', 7, NULL, NULL),
('cnth', 8, NULL, NULL),
('cnth', 9, NULL, NULL),
('cnth', 10, 'vishnu', '1998-11-02'),
('algo', 11, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `name` varchar(50) DEFAULT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) DEFAULT NULL,
  `branch` varchar(20) DEFAULT NULL,
  `year` int(11) NOT NULL,
  `emailid` varchar(30) DEFAULT NULL,
  `contact` varchar(30) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`name`, `username`, `password`, `branch`, `year`, `emailid`, `contact`, `address`) VALUES
('vishnu', 'vishnu', 'vishnu', 'cse', 3, 'vishu@gmail.com', '984909924', 'knl');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`username`);

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`bookid`);

--
-- Indexes for table `book_details`
--
ALTER TABLE `book_details`
  ADD KEY `bookid` (`bookid`),
  ADD KEY `studentid` (`studentid`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`username`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `book_details`
--
ALTER TABLE `book_details`
  ADD CONSTRAINT `book_details_ibfk_1` FOREIGN KEY (`bookid`) REFERENCES `book` (`bookid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `book_details_ibfk_2` FOREIGN KEY (`studentid`) REFERENCES `student` (`username`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
