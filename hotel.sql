-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 04, 2024 at 08:29 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminlogin`
--

CREATE TABLE `adminlogin` (
  `id` int(30) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adminlogin`
--

INSERT INTO `adminlogin` (`id`, `username`, `password`) VALUES
(1, 'prathi', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `id` int(30) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `foodname` varchar(50) NOT NULL,
  `hotelname` varchar(30) NOT NULL,
  `foodprice` varchar(20) NOT NULL,
  `booktype` varchar(40) NOT NULL,
  `quantity` varchar(30) NOT NULL,
  `regdate` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6),
  `status` varchar(50) NOT NULL,
  `usermail` varchar(50) NOT NULL,
  `ownermail` varchar(50) NOT NULL,
  `Ownername` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`id`, `Username`, `foodname`, `hotelname`, `foodprice`, `booktype`, `quantity`, `regdate`, `status`, `usermail`, `ownermail`, `Ownername`) VALUES
(1, 'Bavana', 'Dosai', 'Deepam', '60', 'Table Booking', '2', '2024-03-11 06:17:24.148341', 'New', 'bavana@gmail.com', 'ganesan@gmail.com', 'Ganesan'),
(2, 'Bavana', 'Chiken Noodles', 'Royal Palace', '120', 'Order', '2', '2024-03-11 06:45:53.748660', 'New', 'bavana@gmail.com', 'pranav@gmail.com', 'Pranav');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `id` int(30) NOT NULL,
  `Username` varchar(30) NOT NULL,
  `Hotelname` varchar(50) NOT NULL,
  `rating` varchar(30) NOT NULL,
  `description` varchar(100) NOT NULL,
  `regdate` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`id`, `Username`, `Hotelname`, `rating`, `description`, `regdate`) VALUES
(1, 'Bavana', 'Deepam', '4', 'good', '2024-03-11 06:21:20.473981'),
(2, 'Bavana', 'Royal Palace', '5', 'Very good', '2024-03-11 06:46:50.665672');

-- --------------------------------------------------------

--
-- Table structure for table `food`
--

CREATE TABLE `food` (
  `id` int(30) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Hotelname` varchar(50) NOT NULL,
  `Photo` varchar(30) NOT NULL,
  `Price` varchar(20) NOT NULL,
  `Street` varchar(40) NOT NULL,
  `Ownername` varchar(30) NOT NULL,
  `City` varchar(30) NOT NULL,
  `owneremail` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `food`
--

INSERT INTO `food` (`id`, `Name`, `Hotelname`, `Photo`, `Price`, `Street`, `Ownername`, `City`, `owneremail`) VALUES
(1, 'Dosai', 'Deepam', 'dosai.jfif', '60', 'Gandhi Puram', 'Ganesan', 'coimbatore', 'ganesan@gmail.com'),
(2, 'Chiken Noodles', 'Royal Palace', 'noodles.jfif', '120', 'RS Puram', 'Pranav', 'Coimbatore', 'pranav@gmail.com'),
(3, 'Dosai', 'Royal Palace', 'dosai.jfif', '40', 'RS Puram', 'Pranav', 'Coimbatore', 'pranav@gmail.com'),
(5, 'Falooda', 'Deepam', 'falooda.jfif', '120', 'Gandhi Puram', 'Ganesan', 'Coimbatore', 'ganesan@gmail.com'),
(6, 'Fish Fry', 'Deepam', 'fish fry.jfif', '200', 'Gandhi Puram', 'Ganesan', 'Coimbatore', 'ganesan@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `ownerreg`
--

CREATE TABLE `ownerreg` (
  `id` int(30) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Gender` varchar(50) NOT NULL,
  `Dob` varchar(50) NOT NULL,
  `Hotelname` varchar(50) NOT NULL,
  `Profile` varchar(50) NOT NULL,
  `Emailid` varchar(50) NOT NULL,
  `Phoneno` varchar(50) NOT NULL,
  `Street` varchar(50) NOT NULL,
  `City` varchar(50) NOT NULL,
  `State` varchar(50) NOT NULL,
  `Country` varchar(50) NOT NULL,
  `Operatinghours` varchar(50) NOT NULL,
  `Hotelimage` varchar(50) NOT NULL,
  `regdate` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6),
  `Status` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ownerreg`
--

INSERT INTO `ownerreg` (`id`, `Name`, `Gender`, `Dob`, `Hotelname`, `Profile`, `Emailid`, `Phoneno`, `Street`, `City`, `State`, `Country`, `Operatinghours`, `Hotelimage`, `regdate`, `Status`, `Password`) VALUES
(1, 'Ganesan', 'Male', '1987-06-11', 'Deepam', 'houseowner1.jpg', 'ganesan@gmail.com', '9876543210', 'Gandhi Puram', 'Coimbatore', 'Tamil nadu', 'India', '9:00am to 10:00pm', 'pgh3.jpg', '2024-03-11 06:42:27.512694', 'True', 'Gan876HW'),
(2, 'Pranav', 'Male', '1992-07-01', 'Royal Palace', 'user4.jpg', 'pirathimag1412@gmail.com', '9776543210', 'RS Puram', 'Coimbatore', 'Tamil nadu', 'India', '9:30am to 10:00pm', 'retraunt1.jfif', '2024-03-12 05:10:12.986727', 'True', 'pranav@01'),
(3, 'Sandhya', 'Female', '1998-10-06', 'Bite Spot', 'houseowner4.jpg', 'sandhya@2gmail.com', '8976543210', 'Saibaba Colony', 'Coimbatore', 'Tamil nadu', 'India', '9:30am to 10:00pm', 'restraunt3.jfif', '2024-03-11 06:42:39.912677', 'New', ''),
(4, 'Abinaya', 'Female', '1990-06-06', 'Flavor Nook', 'houseowner2.jpg', 'abinaya@gmail.com', '9776543222', 'RS Puram', 'Coimbatore', 'Tamil nadu', 'India', '9:30am to 10:00pm', 'restraunt2.jfif', '2024-03-11 06:42:42.185889', 'New', '');

-- --------------------------------------------------------

--
-- Table structure for table `userreg`
--

CREATE TABLE `userreg` (
  `id` int(30) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Gender` varchar(30) NOT NULL,
  `Dob` varchar(30) NOT NULL,
  `Profile` varchar(20) NOT NULL,
  `Emailid` varchar(60) NOT NULL,
  `Phoneno` varchar(50) NOT NULL,
  `Street` varchar(50) NOT NULL,
  `City` varchar(50) NOT NULL,
  `State` varchar(50) NOT NULL,
  `Country` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `regdate` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `userreg`
--

INSERT INTO `userreg` (`id`, `Name`, `Gender`, `Dob`, `Profile`, `Emailid`, `Phoneno`, `Street`, `City`, `State`, `Country`, `Password`, `regdate`) VALUES
(1, 'Bavana', 'Female', '2016-06-15', 'houseowner3.jpg', 'bavana@gmail.com', '9876543247', 'SS Nagar', 'coimbatore', 'Tamil Nadu', 'India', 'bava@27', '2024-03-11 05:49:50.518114'),
(2, 'Devi', 'Female', '2001-10-12', 'houseowner5.jpg', 'devisrithangaraj4@gmail.com', '9876543247', 'Saibaba Colony', 'Coimbatore', 'Tamil Nadu', 'India', 'devi@03', '2024-03-11 06:36:11.023887'),
(3, 'Prathima', 'Female', '2000-07-13', 'user3.jpg', 'pirathimag96610@gmail.com', '8956231470', 'SS Nagar', 'Coimbatore', 'Tamil Nadu', 'India', 'prathi', '2024-03-11 06:37:37.179077');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminlogin`
--
ALTER TABLE `adminlogin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `food`
--
ALTER TABLE `food`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ownerreg`
--
ALTER TABLE `ownerreg`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `userreg`
--
ALTER TABLE `userreg`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adminlogin`
--
ALTER TABLE `adminlogin`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `food`
--
ALTER TABLE `food`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `ownerreg`
--
ALTER TABLE `ownerreg`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `userreg`
--
ALTER TABLE `userreg`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
