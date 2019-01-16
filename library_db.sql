-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 16, 2019 at 06:02 AM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `book_id` int(11) NOT NULL,
  `book_isbn` varchar(100) NOT NULL,
  `book_name` varchar(255) NOT NULL,
  `book_publisher` int(11) NOT NULL,
  `book_count` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`book_id`, `book_isbn`, `book_name`, `book_publisher`, `book_count`) VALUES
(1, '978-3-16-148410-0', 'Mathematics in Advanced', 2, 3),
(3, '978-3-16-148410-1', 'Science in Advanced', 2, 5),
(4, '487165', 'uyindjm', 2, 6),
(5, '94856+3', 'buhnijm', 2, 1956),
(6, '874165', '7tbuhyin', 2, 6);

-- --------------------------------------------------------

--
-- Table structure for table `borrow`
--

CREATE TABLE `borrow` (
  `borrow_id` int(11) NOT NULL,
  `borrow_book` int(11) NOT NULL,
  `borrow_member` int(11) NOT NULL,
  `borrow_issued_date` date NOT NULL,
  `borrow_due_date` date NOT NULL,
  `borrow_return_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `borrow`
--

INSERT INTO `borrow` (`borrow_id`, `borrow_book`, `borrow_member`, `borrow_issued_date`, `borrow_due_date`, `borrow_return_date`) VALUES
(2, 1, 1, '2019-01-16', '2019-01-30', '2019-01-29'),
(3, 5, 2, '2019-01-18', '2019-02-05', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `mem_id` int(11) NOT NULL,
  `mem_name` varchar(100) NOT NULL,
  `mem_type` varchar(20) NOT NULL,
  `mem_address` varchar(255) DEFAULT NULL,
  `mem_phone` varchar(12) DEFAULT NULL,
  `mem_email` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `member`
--

INSERT INTO `member` (`mem_id`, `mem_name`, `mem_type`, `mem_address`, `mem_phone`, `mem_email`) VALUES
(1, 'Aruna Jayakodi', '1 year', '97, Main Street, Ja-ela', '077-1234567', 'arunajayakodi@gmail.com'),
(2, 'gbhjn', 'hbnkj', 'hknj', 'bhjkm', 'bhnk');

-- --------------------------------------------------------

--
-- Table structure for table `publisher`
--

CREATE TABLE `publisher` (
  `publisher_id` int(11) NOT NULL,
  `publisher_name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `publisher`
--

INSERT INTO `publisher` (`publisher_id`, `publisher_name`) VALUES
(2, 'Senerath Abedira');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`book_id`),
  ADD UNIQUE KEY `book_isbn` (`book_isbn`),
  ADD KEY `book_publisher` (`book_publisher`);

--
-- Indexes for table `borrow`
--
ALTER TABLE `borrow`
  ADD PRIMARY KEY (`borrow_id`),
  ADD KEY `borrow_book` (`borrow_book`,`borrow_member`),
  ADD KEY `fk_mem_to_borr` (`borrow_member`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`mem_id`);

--
-- Indexes for table `publisher`
--
ALTER TABLE `publisher`
  ADD PRIMARY KEY (`publisher_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `book`
--
ALTER TABLE `book`
  MODIFY `book_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `borrow`
--
ALTER TABLE `borrow`
  MODIFY `borrow_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `member`
--
ALTER TABLE `member`
  MODIFY `mem_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `publisher`
--
ALTER TABLE `publisher`
  MODIFY `publisher_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `book`
--
ALTER TABLE `book`
  ADD CONSTRAINT `fk_pub_to_book` FOREIGN KEY (`book_publisher`) REFERENCES `publisher` (`publisher_id`);

--
-- Constraints for table `borrow`
--
ALTER TABLE `borrow`
  ADD CONSTRAINT `fk_book_to_borr` FOREIGN KEY (`borrow_book`) REFERENCES `book` (`book_id`),
  ADD CONSTRAINT `fk_mem_to_borr` FOREIGN KEY (`borrow_member`) REFERENCES `member` (`mem_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
