-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 20, 2018 at 11:48 AM
-- Server version: 10.1.30-MariaDB
-- PHP Version: 7.2.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `food`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `role` varchar(15) NOT NULL DEFAULT 'Customer',
  `name` varchar(15) NOT NULL,
  `username` varchar(10) NOT NULL,
  `password` varchar(16) NOT NULL,
  `email` varchar(35) DEFAULT NULL,
  `address` varchar(300) DEFAULT NULL,
  `contact` bigint(11) NOT NULL,
  `verified` tinyint(1) NOT NULL DEFAULT '0',
  `deleted` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `role`, `name`, `username`, `password`, `email`, `address`, `contact`, `verified`, `deleted`) VALUES
(2, 'Customer', 'Customer 1', 'user1', 'pass1', 'mail2@example.com', 'Address 2', 9898000001, 1, 0),
(3, 'Customer', 'Customer 2', 'user2', 'pass2', 'mail3@example.com', 'Address 3', 9898000002, 1, 0),
(4, 'Customer', 'Customer 3', 'user3', 'pass3', '', '', 9898000003, 0, 0),
(5, 'Customer', 'Customer 4', 'user4', 'pass4', '', '', 9898000004, 0, 1),
(6, 'Customer', 'Milind Shah', 'milind', 'milind', NULL, NULL, 9876543210, 1, 0),
(7, 'Customer', 'prtk', 'prtk', 'prtk1910', NULL, NULL, 9619775837, 0, 0),
(8, 'Customer', 'test', 'testcustom', '1234', 'test@test.com', 'Mumbai', 9876543210, 1, 0),
(9, 'Customer', 'newuser1', 'newuser1', 'newuser1', 'newuser1@gmail.com', 'Mumbai', 9876543210, 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `role` varchar(15) NOT NULL DEFAULT 'Customer',
  `name` varchar(15) NOT NULL,
  `username` varchar(10) NOT NULL,
  `password` varchar(16) NOT NULL,
  `email` varchar(35) DEFAULT NULL,
  `address` varchar(300) DEFAULT NULL,
  `contact` bigint(11) NOT NULL,
  `verified` tinyint(1) NOT NULL DEFAULT '0',
  `deleted` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`id`, `role`, `name`, `username`, `password`, `email`, `address`, `contact`, `verified`, `deleted`) VALUES
(1, 'Administrator', 'Admin 1', 'root', 'toor', '', 'Address 1', 9898000000, 1, 0),
(7, 'Employee', 'test', 'testemp', '1234', 'test@test.com', 'Mumbai', 9877654321, 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE `items` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `price` int(11) NOT NULL,
  `deleted` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `items`
--

INSERT INTO `items` (`id`, `name`, `price`, `deleted`) VALUES
(1, 'Item 1', 25, 1),
(2, 'Item 2', 45, 0),
(3, 'Item 3', 20, 0),
(4, 'Item 4', 15, 1),
(5, 'Item 5', 20, 0),
(6, 'Item 88', 500, 0);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `address` varchar(300) NOT NULL,
  `description` varchar(300) NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `payment_type` varchar(16) NOT NULL DEFAULT 'Wallet',
  `total` int(11) NOT NULL,
  `status` varchar(25) NOT NULL DEFAULT 'Yet to be delivered',
  `deleted` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`id`, `customer_id`, `address`, `description`, `date`, `payment_type`, `total`, `status`, `deleted`) VALUES
(1, 2, 'Address 2', 'Sample Description 1', '2017-03-28 17:32:41', 'Wallet', 150, 'Delivered', 0),
(2, 2, 'New address 2', '', '2017-03-28 17:43:05', 'Wallet', 130, 'Cancelled by Customer', 1),
(3, 3, 'Address 3', 'Sample Description 2', '2017-03-28 19:49:33', 'Cash On Delivery', 130, 'Delivered', 0),
(4, 3, 'Address 3', '', '2017-03-28 19:52:01', 'Cash On Delivery', 130, 'Cancelled by Customer', 1),
(5, 3, 'New Address 3', '', '2017-03-28 20:47:28', 'Wallet', 285, 'Paused', 0),
(6, 3, 'New Address 3', '', '2017-03-30 00:43:31', 'Wallet', 325, 'Cancelled by Customer', 1),
(7, 2, 'Address 2', '', '2018-09-20 10:26:11', 'Cash On Delivery', 105, 'Cancelled by Customer', 1),
(8, 6, 'aaaaa', '', '2018-09-20 19:07:37', 'Wallet', 85, 'Yet to be delivered', 0),
(9, 8, 'Mumbai', '', '2018-09-24 18:15:01', 'Cash On Delivery', 345, 'Delivered', 0),
(10, 9, 'Mumbai', '', '2018-09-29 10:39:54', 'Cash On Delivery', 85, 'Yet to be delivered', 0),
(11, 8, 'Mumbai', '', '2018-10-08 10:22:46', 'Cash On Delivery', 605, 'Yet to be delivered', 0),
(12, 8, 'Mumbai', '', '2018-10-08 10:23:11', 'Cash On Delivery', 0, 'Yet to be delivered', 0);

-- --------------------------------------------------------

--
-- Table structure for table `order_details`
--

CREATE TABLE `order_details` (
  `id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `order_details`
--

INSERT INTO `order_details` (`id`, `order_id`, `item_id`, `quantity`, `price`) VALUES
(1, 1, 2, 2, 90),
(2, 1, 3, 3, 60),
(3, 2, 2, 2, 90),
(4, 2, 3, 2, 40),
(5, 3, 2, 2, 90),
(6, 3, 3, 2, 40),
(7, 4, 2, 2, 90),
(8, 4, 3, 2, 40),
(9, 5, 2, 5, 225),
(10, 5, 3, 2, 40),
(11, 5, 5, 1, 20),
(12, 6, 2, 5, 225),
(13, 6, 3, 3, 60),
(14, 6, 5, 2, 40),
(15, 7, 2, 1, 45),
(16, 7, 3, 2, 40),
(17, 7, 5, 1, 20),
(18, 8, 2, 1, 45),
(19, 8, 3, 1, 20),
(20, 8, 5, 1, 20),
(21, 9, 2, 5, 225),
(22, 9, 3, 4, 80),
(23, 9, 5, 2, 40),
(24, 10, 2, 1, 45),
(25, 10, 3, 1, 20),
(26, 10, 5, 1, 20),
(27, 11, 6, 1, 500),
(28, 11, 2, 1, 45),
(29, 11, 3, 2, 40),
(30, 11, 5, 1, 20);

-- --------------------------------------------------------

--
-- Table structure for table `tickets`
--

CREATE TABLE `tickets` (
  `id` int(11) NOT NULL,
  `poster_id` int(11) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `description` varchar(3000) NOT NULL,
  `status` varchar(8) NOT NULL DEFAULT 'Open',
  `type` varchar(30) NOT NULL DEFAULT 'Others',
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `deleted` tinyint(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tickets`
--

INSERT INTO `tickets` (`id`, `poster_id`, `subject`, `description`, `status`, `type`, `date`, `deleted`) VALUES
(1, 2, 'Subject 1', 'New Description for Subject 1', 'Answered', 'Support', '2017-03-30 18:08:51', 0);

-- --------------------------------------------------------

--
-- Table structure for table `ticket_details`
--

CREATE TABLE `ticket_details` (
  `id` int(11) NOT NULL,
  `ticket_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ticket_details`
--

INSERT INTO `ticket_details` (`id`, `ticket_id`, `user_id`, `description`, `date`) VALUES
(1, 1, 2, 'New Description for Subject 1', '2017-03-30 18:08:51'),
(2, 1, 2, 'Reply-1 for Subject 1', '2017-03-30 19:59:09');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `order_details`
--
ALTER TABLE `order_details`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `item_id` (`item_id`),
  ADD KEY `order_id` (`order_id`);

--
-- Indexes for table `tickets`
--
ALTER TABLE `tickets`
  ADD PRIMARY KEY (`id`),
  ADD KEY `poster_id` (`poster_id`);

--
-- Indexes for table `ticket_details`
--
ALTER TABLE `ticket_details`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ticket_id` (`ticket_id`),
  ADD KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `items`
--
ALTER TABLE `items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `order_details`
--
ALTER TABLE `order_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `tickets`
--
ALTER TABLE `tickets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `ticket_details`
--
ALTER TABLE `ticket_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`);

--
-- Constraints for table `order_details`
--
ALTER TABLE `order_details`
  ADD CONSTRAINT `order_details_ibfk_1` FOREIGN KEY (`item_id`) REFERENCES `items` (`id`),
  ADD CONSTRAINT `order_details_ibfk_2` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`);

--
-- Constraints for table `tickets`
--
ALTER TABLE `tickets`
  ADD CONSTRAINT `tickets_ibfk_1` FOREIGN KEY (`poster_id`) REFERENCES `customer` (`id`);

--
-- Constraints for table `ticket_details`
--
ALTER TABLE `ticket_details`
  ADD CONSTRAINT `ticket_details_ibfk_1` FOREIGN KEY (`ticket_id`) REFERENCES `tickets` (`id`),
  ADD CONSTRAINT `ticket_details_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `customer` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
