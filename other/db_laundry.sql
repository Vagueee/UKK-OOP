-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 17, 2023 at 02:53 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_laundry`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `detailselectbyid` (IN `id_tr` INT)   BEGIN
SELECT tb_detail_transaksi.id_paket, tb_detail_transaksi.qty, tb_detail_transaksi.keterangan, (harga) * qty AS total FROM tb_detail_transaksi JOIN tb_paket ON tb_detail_transaksi.id_paket=tb_paket.id_paket WHERE tb_detail_transaksi.id_transaksi=id_tr;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `detailtambah` (IN `id_tr` INT, IN `id_pk` INT, IN `qty_tr` VARCHAR(255), IN `ket_tr` VARCHAR(255))   BEGIN
INSERT INTO tb_detail_transaksi(id_transaksi, id_paket, qty, keterangan) VALUES(id_tr, id_pk, qty_tr, ket_tr);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `dropdownkasir` ()   BEGIN
SELECT id_user, nama FROM tb_user;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `dropdownoutlet` ()   BEGIN
SELECT id_outlet, nama FROM tb_outlet;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `dropdownpaket` ()   BEGIN
SELECT id_paket, nama_paket FROM tb_paket;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `dropdownpelanggan` ()   BEGIN
SELECT id_member, nama FROM tb_member;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `karyawandelete` (IN `id_kar` INT)   BEGIN
DELETE FROM tb_user WHERE id_user=id_kar;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `karyawanedit` (`id_kar` INT, `id_out` INT, `nama_kar` VARCHAR(255), `username_kar` VARCHAR(255), `password_kar` VARCHAR(255), `role_kar` ENUM('admin','kasir','owner'))   BEGIN 
UPDATE tb_user SET id_outlet = id_out, nama = nama_kar, username = username_kar, password = password_kar, role = role_kar 
WHERE id_user = id_kar;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `karyawanrole` ()   BEGIN
SHOW COLUMNS FROM tb_user WHERE FIELD='role';
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `karyawanselect` ()   BEGIN
SELECT tb_user.`id_user`, tb_outlet.nama, tb_user.`nama`, tb_user.`username`, tb_user.`role`
FROM tb_user JOIN tb_outlet ON tb_user.id_outlet=tb_outlet.id_outlet;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `karyawanselectbyid` (IN `id_kar` INT)   BEGIN
SELECT tb_user.`id_user`, tb_outlet.id_outlet, tb_user.`nama`, tb_user.`username`, tb_user.`password`, tb_user.`role`
FROM tb_user JOIN tb_outlet ON tb_user.id_outlet=tb_outlet.id_outlet
WHERE id_user = id_kar;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `karyawantambah` (`id_out` INT, `nama_kar` VARCHAR(255), `username_kar` VARCHAR(255), `password_kar` VARCHAR(255), `role_kar` ENUM('admin','kasir','owner'))   BEGIN
INSERT INTO tb_user(id_outlet, nama, username, password, role) VALUES(id_out, nama_kar, username_kar, password_kar, role_kar);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `login` (`user` VARCHAR(255), `pass` VARCHAR(255))   BEGIN
SELECT * FROM tb_user WHERE username=user AND password=pass;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `outletdelete` (IN `id_out` INT)   BEGIN
DELETE FROM tb_outlet WHERE id_outlet=id_out;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `outletedit` (IN `id_out` INT, IN `nama_out` VARCHAR(255), IN `alamat_out` TEXT, IN `tlp_out` VARCHAR(15))   BEGIN 
UPDATE tb_outlet SET nama = nama_out, alamat = alamat_out, tlp = tlp_out 
WHERE id_outlet = id_out;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `outletselect` ()   BEGIN
SELECT * FROM tb_outlet;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `outletselectbyid` (IN `id_out` INT)   BEGIN
SELECT * FROM tb_outlet WHERE id_outlet = id_out;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `outlettambah` (IN `nama_out` VARCHAR(255), IN `alamat_out` TEXT, IN `tlp_out` VARCHAR(15))   BEGIN 
INSERT INTO tb_outlet(nama, alamat, tlp) VALUES(nama_out, alamat_out, tlp_out);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pelanggandelete` (`id_pel` INT)   BEGIN
DELETE FROM tb_member WHERE id_member=id_pel;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pelangganedit` (`id_pel` INT, `nama_pel` VARCHAR(255), `alamat_pel` TEXT, `jenis_kelamin_pel` ENUM('L','P'), `tlp_pel` VARCHAR(15))   BEGIN 
UPDATE tb_member SET nama = nama_pel, alamat = alamat_pel, jenis_kelamin = jenis_kelamin_pel, tlp = tlp_pel
WHERE id_member = id_pel;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pelangganjk` ()   BEGIN
SHOW COLUMNS FROM tb_member WHERE FIELD='jenis_kelamin';
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pelangganselect` ()   BEGIN 
SELECT * FROM tb_member;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pelangganselectbyid` (`id_pel` INT)   BEGIN
SELECT * FROM tb_member WHERE id_member = id_pel;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pelanggantambah` (IN `nama_pel` VARCHAR(100), IN `alamat_pel` TEXT, IN `jeniskelamin_pel` ENUM('L','P'), IN `tlp_pel` VARCHAR(15))   BEGIN 
INSERT INTO tb_member(nama, alamat, jenis_kelamin, tlp) VALUES(nama_pel, alamat_pel, jeniskelamin_pel, tlp_pel);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `transaksidelete` (IN `id_tr` INT)   BEGIN
DELETE FROM tb_transaksi WHERE id_transaksi=id_tr;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `transaksidibayar` ()   BEGIN
SHOW COLUMNS FROM tb_transaksi WHERE FIELD='dibayar';
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `transaksiedit` (`id_tr` INT, `status_tr` ENUM('baru','proses','selesai','belajar'), `dibayar_tr` ENUM('dibayar','belum_dibayar'))   BEGIN
UPDATE tb_transaksi SET status = status_tr, dibayar = dibayar_tr
WHERE id_transaksi = id_tr;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `transaksiselect` ()   BEGIN
SELECT tb_transaksi.id_transaksi, tb_transaksi.kode_invoice, tb_outlet.nama, tb_user.nama, tb_member.nama, tb_transaksi.tgl, tb_transaksi.batas_waktu, tb_transaksi.waktu_bayar, tb_transaksi.status, tb_transaksi.dibayar
FROM tb_transaksi JOIN tb_outlet ON tb_transaksi.id_outlet=tb_outlet.id_outlet JOIN tb_user ON tb_transaksi.id_user=tb_user.id_user JOIN tb_member ON tb_transaksi.id_member=tb_member.id_member;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `transaksiselectbyid` (IN `id_tr` INT)   BEGIN
SELECT * FROM tb_transaksi WHERE id_transaksi=id_tr;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `transaksistatus` ()   BEGIN
SHOW COLUMNS FROM tb_transaksi WHERE FIELD='status';
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `transaksitambah` (IN `invoice_tr` VARCHAR(255), IN `id_out_tr` INT, IN `id_user_tr` INT, IN `id_member_tr` INT, IN `tgl_tr` DATE, IN `batas_waktu_tr` DATE, IN `waktu_bayar_tr` DATE, IN `biaya_tambahan_tr` VARCHAR(255), IN `diskon_tr` VARCHAR(255), IN `status_tr` ENUM('baru','proses','selesai','diambil'), IN `dibayar_tr` ENUM('dibayar','belum_dibayar'))   BEGIN
INSERT INTO tb_transaksi(kode_invoice, id_outlet, id_user, id_member, tgl, batas_waktu, waktu_bayar, biaya_tambahan, diskon, status, dibayar)
VALUES(invoice_tr, id_out_tr, id_user_tr, id_member_tr, tgl_tr, batas_waktu_tr, waktu_bayar_tr, biaya_tambahan_tr, diskon_tr, status_tr, dibayar_tr);
END$$

--
-- Functions
--
CREATE DEFINER=`root`@`localhost` FUNCTION `lasttr` (`id_member` INT(11)) RETURNS DATE  BEGIN
       DECLARE laster DATE;
       SELECT max(tgl) INTO laster FROM tb_transaksi
       WHERE id_member=id_member;
       RETURN laster;
   END$$

CREATE DEFINER=`root`@`localhost` FUNCTION `totalpaket` () RETURNS INT(11)  BEGIN
DECLARE jumlah INT;
SELECT COUNT(*) INTO jumlah FROM tb_paket;
RETURN jumlah;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `log_transaksi`
--

CREATE TABLE `log_transaksi` (
  `id_aksi` int(15) NOT NULL,
  `id_transaksi` int(15) NOT NULL,
  `aksi` varchar(255) NOT NULL,
  `waktu_aksi` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `log_transaksi`
--

INSERT INTO `log_transaksi` (`id_aksi`, `id_transaksi`, `aksi`, `waktu_aksi`) VALUES
(7, 6, 'Tambah Data Transaksi', '2023-03-15 13:38:16'),
(8, 6, 'Update Data Transaksi', '2023-03-15 13:40:26'),
(9, 6, 'Delete Data Transaksi', '2023-03-15 13:40:55'),
(10, 7, 'Tambah Data Transaksi', '2023-03-16 09:10:53'),
(11, 7, 'Delete Data Transaksi', '2023-03-16 09:13:17'),
(12, 8, 'Tambah Data Transaksi', '2023-03-16 11:40:14'),
(13, 9, 'Tambah Data Transaksi', '2023-03-16 11:40:54'),
(14, 8, 'Delete Data Transaksi', '2023-03-16 11:41:15'),
(15, 9, 'Delete Data Transaksi', '2023-03-16 11:41:17'),
(16, 1, 'Update Data Transaksi', '2023-03-16 11:42:51'),
(17, 2, 'Update Data Transaksi', '2023-03-16 11:42:57'),
(18, 2, 'Update Data Transaksi', '2023-03-16 13:30:27'),
(19, 10, 'Tambah Data Transaksi', '2023-03-16 14:09:43'),
(20, 11, 'Tambah Data Transaksi', '2023-03-16 14:12:41'),
(21, 10, 'Delete Data Transaksi', '2023-03-16 14:15:32'),
(22, 11, 'Delete Data Transaksi', '2023-03-16 14:15:33'),
(23, 12, 'Tambah Data Transaksi', '2023-03-16 14:18:34'),
(24, 13, 'Tambah Data Transaksi', '2023-03-16 14:20:11'),
(25, 12, 'Delete Data Transaksi', '2023-03-16 14:20:51'),
(26, 13, 'Delete Data Transaksi', '2023-03-16 14:20:53'),
(27, 14, 'Tambah Data Transaksi', '2023-03-16 14:23:49'),
(28, 15, 'Tambah Data Transaksi', '2023-03-16 14:25:31'),
(29, 14, 'Delete Data Transaksi', '2023-03-16 14:26:51'),
(30, 15, 'Delete Data Transaksi', '2023-03-16 14:26:53'),
(31, 16, 'Tambah Data Transaksi', '2023-03-16 14:27:23'),
(32, 17, 'Tambah Data Transaksi', '2023-03-16 14:28:15'),
(33, 16, 'Delete Data Transaksi', '2023-03-16 14:28:52'),
(34, 18, 'Tambah Data Transaksi', '2023-03-17 08:27:16'),
(35, 18, 'Update Data Transaksi', '2023-03-17 08:34:07');

-- --------------------------------------------------------

--
-- Table structure for table `tb_detail_transaksi`
--

CREATE TABLE `tb_detail_transaksi` (
  `id_det_transaksi` int(11) NOT NULL,
  `id_transaksi` int(11) DEFAULT NULL,
  `id_paket` int(11) DEFAULT NULL,
  `qty` int(11) DEFAULT NULL,
  `keterangan` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_detail_transaksi`
--

INSERT INTO `tb_detail_transaksi` (`id_det_transaksi`, `id_transaksi`, `id_paket`, `qty`, `keterangan`) VALUES
(1, 1, 1, 1, 'Cuci bed cover'),
(2, 2, 2, 3, 'kilos'),
(3, 17, 3, 3, '2 Selimut Tebal, 1 Selimut Tipis'),
(4, 18, 2, 2, '2 Kilo Seragam Sekolah');

-- --------------------------------------------------------

--
-- Table structure for table `tb_member`
--

CREATE TABLE `tb_member` (
  `id_member` int(11) NOT NULL,
  `nama` varchar(100) DEFAULT NULL,
  `alamat` text DEFAULT NULL,
  `jenis_kelamin` enum('L','P') DEFAULT NULL,
  `tlp` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_member`
--

INSERT INTO `tb_member` (`id_member`, `nama`, `alamat`, `jenis_kelamin`, `tlp`) VALUES
(1, 'Kita', 'Jl. Kitaaaan No.1', 'P', '081234567890'),
(2, 'Ikuyo', 'Jl. Kitaaaan No.2', 'L', '081234567891'),
(5, 'Kanaha', 'Kanayanser', 'L', '0812'),
(6, 'TEsT', 'Jl. Tesaj', 'P', '08192837465');

-- --------------------------------------------------------

--
-- Table structure for table `tb_outlet`
--

CREATE TABLE `tb_outlet` (
  `id_outlet` int(11) NOT NULL,
  `nama` varchar(100) DEFAULT NULL,
  `alamat` text DEFAULT NULL,
  `tlp` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_outlet`
--

INSERT INTO `tb_outlet` (`id_outlet`, `nama`, `alamat`, `tlp`) VALUES
(1, 'UKK', 'Jl. UKK.jpg', '081234567890'),
(2, 'Hashimoto', 'Jl. Tokyo No.2', '081234567888'),
(5, 'Radity', 'Jl. Kanana', '08987654321');

-- --------------------------------------------------------

--
-- Table structure for table `tb_paket`
--

CREATE TABLE `tb_paket` (
  `id_paket` int(11) NOT NULL,
  `id_outlet` int(11) DEFAULT NULL,
  `jenis` enum('kiloan','selimut','bed_cover','kaos','lain') DEFAULT NULL,
  `nama_paket` varchar(100) DEFAULT NULL,
  `harga` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_paket`
--

INSERT INTO `tb_paket` (`id_paket`, `id_outlet`, `jenis`, `nama_paket`, `harga`) VALUES
(1, 1, 'bed_cover', 'Turu cover', 50000),
(2, 1, 'kiloan', 'Kilos', 10000),
(3, 1, 'selimut', 'Selimute', 49999);

-- --------------------------------------------------------

--
-- Table structure for table `tb_transaksi`
--

CREATE TABLE `tb_transaksi` (
  `id_transaksi` int(11) NOT NULL,
  `kode_invoice` varchar(100) DEFAULT NULL,
  `id_outlet` int(11) DEFAULT NULL,
  `id_user` int(11) DEFAULT NULL,
  `id_member` int(11) DEFAULT NULL,
  `tgl` date DEFAULT NULL,
  `batas_waktu` date DEFAULT NULL,
  `waktu_bayar` date DEFAULT NULL,
  `biaya_tambahan` int(11) DEFAULT NULL,
  `diskon` int(11) DEFAULT NULL,
  `status` enum('baru','proses','selesai','diambil') DEFAULT NULL,
  `dibayar` enum('dibayar','belum_dibayar') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_transaksi`
--

INSERT INTO `tb_transaksi` (`id_transaksi`, `kode_invoice`, `id_outlet`, `id_user`, `id_member`, `tgl`, `batas_waktu`, `waktu_bayar`, `biaya_tambahan`, `diskon`, `status`, `dibayar`) VALUES
(1, 'L000001', 1, 1, 1, '2023-02-21', '2023-02-21', '2023-02-21', 0, 0, 'selesai', 'dibayar'),
(2, 'L000002', 1, 1, 2, '2023-02-21', '2023-02-21', '2023-02-21', 0, 0, 'selesai', 'belum_dibayar'),
(17, 'L000011', 1, 7, 6, '2023-03-16', '2023-03-17', '2023-03-16', 0, 0, 'baru', 'belum_dibayar'),
(18, 'L000012', 5, 4, 5, '2023-03-17', '2023-03-20', '2023-03-17', 0, 0, 'proses', 'belum_dibayar');

--
-- Triggers `tb_transaksi`
--
DELIMITER $$
CREATE TRIGGER `log_transaksi_delete` AFTER DELETE ON `tb_transaksi` FOR EACH ROW BEGIN
INSERT INTO log_transaksi(id_transaksi, aksi, waktu_aksi) VALUES (old.id_transaksi, "Delete Data Transaksi" , NOW());
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `log_transaksi_tambah` AFTER INSERT ON `tb_transaksi` FOR EACH ROW BEGIN
INSERT INTO log_transaksi(id_transaksi, aksi, waktu_aksi) VALUES (new.id_transaksi, "Tambah Data Transaksi" , NOW());
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `log_transaksi_update` AFTER UPDATE ON `tb_transaksi` FOR EACH ROW BEGIN
INSERT INTO log_transaksi(id_transaksi, aksi, waktu_aksi) VALUES (old.id_transaksi, "Update Data Transaksi" , NOW());
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `tb_user`
--

CREATE TABLE `tb_user` (
  `id_user` int(11) NOT NULL,
  `id_outlet` int(11) DEFAULT NULL,
  `nama` varchar(100) DEFAULT NULL,
  `username` varchar(30) DEFAULT NULL,
  `password` text DEFAULT NULL,
  `role` enum('admin','kasir','owner') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_user`
--

INSERT INTO `tb_user` (`id_user`, `id_outlet`, `nama`, `username`, `password`, `role`) VALUES
(1, 1, 'kiko', 'kiko', 'kiko', 'admin'),
(2, 1, 'mika', 'mika', 'mika', 'kasir'),
(4, 1, 'kira', 'kira', 'kira', 'owner'),
(6, 1, 'Kena', 'Kenahaya', 'Kenahaya', 'owner'),
(7, 2, 'VcV', 'tuyu', 'tuyu', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `log_transaksi`
--
ALTER TABLE `log_transaksi`
  ADD PRIMARY KEY (`id_aksi`);

--
-- Indexes for table `tb_detail_transaksi`
--
ALTER TABLE `tb_detail_transaksi`
  ADD PRIMARY KEY (`id_det_transaksi`),
  ADD KEY `id_transaksi` (`id_transaksi`,`id_paket`),
  ADD KEY `id_paket` (`id_paket`);

--
-- Indexes for table `tb_member`
--
ALTER TABLE `tb_member`
  ADD PRIMARY KEY (`id_member`);

--
-- Indexes for table `tb_outlet`
--
ALTER TABLE `tb_outlet`
  ADD PRIMARY KEY (`id_outlet`);

--
-- Indexes for table `tb_paket`
--
ALTER TABLE `tb_paket`
  ADD PRIMARY KEY (`id_paket`),
  ADD KEY `id_outlet` (`id_outlet`);

--
-- Indexes for table `tb_transaksi`
--
ALTER TABLE `tb_transaksi`
  ADD PRIMARY KEY (`id_transaksi`),
  ADD KEY `id_outlet` (`id_outlet`,`id_member`,`id_user`),
  ADD KEY `id_member` (`id_member`),
  ADD KEY `id_user` (`id_user`);

--
-- Indexes for table `tb_user`
--
ALTER TABLE `tb_user`
  ADD PRIMARY KEY (`id_user`),
  ADD KEY `id_outlet` (`id_outlet`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `log_transaksi`
--
ALTER TABLE `log_transaksi`
  MODIFY `id_aksi` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `tb_detail_transaksi`
--
ALTER TABLE `tb_detail_transaksi`
  MODIFY `id_det_transaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `tb_member`
--
ALTER TABLE `tb_member`
  MODIFY `id_member` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tb_outlet`
--
ALTER TABLE `tb_outlet`
  MODIFY `id_outlet` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tb_paket`
--
ALTER TABLE `tb_paket`
  MODIFY `id_paket` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `tb_transaksi`
--
ALTER TABLE `tb_transaksi`
  MODIFY `id_transaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `tb_user`
--
ALTER TABLE `tb_user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tb_detail_transaksi`
--
ALTER TABLE `tb_detail_transaksi`
  ADD CONSTRAINT `tb_detail_transaksi_ibfk_1` FOREIGN KEY (`id_transaksi`) REFERENCES `tb_transaksi` (`id_transaksi`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tb_detail_transaksi_ibfk_2` FOREIGN KEY (`id_paket`) REFERENCES `tb_paket` (`id_paket`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tb_paket`
--
ALTER TABLE `tb_paket`
  ADD CONSTRAINT `tb_paket_ibfk_1` FOREIGN KEY (`id_outlet`) REFERENCES `tb_outlet` (`id_outlet`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tb_transaksi`
--
ALTER TABLE `tb_transaksi`
  ADD CONSTRAINT `tb_transaksi_ibfk_1` FOREIGN KEY (`id_member`) REFERENCES `tb_member` (`id_member`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tb_transaksi_ibfk_2` FOREIGN KEY (`id_outlet`) REFERENCES `tb_outlet` (`id_outlet`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `tb_transaksi_ibfk_3` FOREIGN KEY (`id_user`) REFERENCES `tb_user` (`id_user`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tb_user`
--
ALTER TABLE `tb_user`
  ADD CONSTRAINT `tb_user_ibfk_1` FOREIGN KEY (`id_outlet`) REFERENCES `tb_outlet` (`id_outlet`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
