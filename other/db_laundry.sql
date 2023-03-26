-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 26, 2023 at 04:30 PM
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
CREATE DEFINER=`root`@`localhost` PROCEDURE `detailidtransaksi` ()   BEGIN
SELECT id_transaksi FROM tb_transaksi ORDER BY id_transaksi DESC LIMIT 1;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `detailselectbyid` (IN `id_tr` INT)   BEGIN
SELECT tb_transaksi.kode_invoice, tb_transaksi.tgl, tb_member.nama AS nama_pel, tb_member.alamat AS alamat_pel, tb_member.tlp AS telp_pel, tb_outlet.nama AS nama_out, tb_outlet.alamat AS alamat_out, tb_outlet.tlp AS telp_out, tb_paket.nama_paket, tb_detail_transaksi.keterangan, tb_detail_transaksi.qty, (tb_detail_transaksi.qty * tb_paket.harga) AS harga, tb_transaksi.biaya_tambahan, tb_transaksi.diskon, (((tb_paket.harga * tb_detail_transaksi.qty) - ((tb_paket.harga * tb_detail_transaksi.qty) * tb_transaksi.diskon / 100)) + tb_transaksi.biaya_tambahan) AS total 
FROM tb_detail_transaksi JOIN tb_paket ON tb_detail_transaksi.id_paket=tb_paket.id_paket JOIN tb_transaksi ON tb_detail_transaksi.id_transaksi=tb_transaksi.id_transaksi JOIN tb_member ON tb_transaksi.id_member=tb_member.id_member JOIN tb_outlet ON tb_transaksi.id_outlet=tb_outlet.id_outlet

WHERE tb_detail_transaksi.id_transaksi=id_tr;
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
FROM tb_user JOIN tb_outlet ON tb_user.id_outlet=tb_outlet.id_outlet
ORDER BY tb_user.id_user ASC;
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
SELECT * FROM tb_outlet
ORDER BY tb_outlet.id_outlet ASC;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `outletselectbyid` (IN `id_out` INT)   BEGIN
SELECT * FROM tb_outlet WHERE id_outlet = id_out;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `outlettambah` (IN `nama_out` VARCHAR(255), IN `alamat_out` TEXT, IN `tlp_out` VARCHAR(15))   BEGIN 
INSERT INTO tb_outlet(nama, alamat, tlp) VALUES(nama_out, alamat_out, tlp_out);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `paketdelete` (IN `id_pk` INT)   BEGIN
DELETE FROM tb_paket WHERE id_paket=id_pk;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `paketedit` (IN `id_pk` INT, IN `id_out` INT, IN `jenis_pk` ENUM('kiloan','selimut','bed_cover','kaos','lain'), IN `nama_pk` VARCHAR(255), IN `harga_pk` INT)   BEGIN
UPDATE tb_paket SET id_outlet=id_out, jenis=jenis_pk, nama_paket=nama_pk, harga=harga_pk
WHERE id_paket=id_pk; 
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `paketjenis` ()   BEGIN
SHOW COLUMNS FROM tb_paket WHERE FIELD='jenis';
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `paketselect` ()   BEGIN
SELECT tb_paket.id_paket, tb_outlet.nama, tb_paket.jenis, tb_paket.nama_paket, tb_paket.harga
FROM tb_paket JOIN tb_outlet ON tb_paket.id_outlet=tb_outlet.id_outlet
ORDER BY tb_paket.id_paket ASC; 
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `paketselectbyid` (IN `id_pk` INT)   BEGIN
SELECT tb_paket.id_paket, tb_outlet.nama, tb_paket.jenis, tb_paket.nama_paket, tb_paket.harga
FROM tb_paket JOIN tb_outlet ON tb_paket.id_outlet=tb_outlet.id_outlet WHERE id_paket=id_pk; 
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pakettambah` (IN `id_out` INT, IN `jenis_pk` ENUM('kiloan','selimut','bed_cover','kaos','lain'), IN `nama_pk` VARCHAR(255), IN `harga_pk` INT)   BEGIN
INSERT INTO tb_paket(id_outlet, jenis, nama_paket, harga) VALUES(id_out, jenis_pk, nama_pk, harga_pk);
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
SELECT * FROM tb_member
ORDER BY tb_member.id_member;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pelangganselectbyid` (`id_pel` INT)   BEGIN
SELECT * FROM tb_member WHERE id_member = id_pel;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pelanggantambah` (IN `nama_pel` VARCHAR(100), IN `alamat_pel` TEXT, IN `jeniskelamin_pel` ENUM('L','P'), IN `tlp_pel` VARCHAR(15))   BEGIN 
INSERT INTO tb_member(nama, alamat, jenis_kelamin, tlp) VALUES(nama_pel, alamat_pel, jeniskelamin_pel, tlp_pel);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pendapatan` ()   BEGIN
select sum(((tb_paket.harga * tb_detail_transaksi.qty) - ((tb_paket.harga * tb_detail_transaksi.qty) * tb_transaksi.diskon / 100)) + tb_transaksi.biaya_tambahan) as pendapatan, CAST(tb_transaksi.tgl AS DATE) as tanggal from tb_detail_transaksi JOIN tb_paket ON tb_detail_transaksi.id_paket=tb_paket.id_paket JOIN tb_transaksi on tb_detail_transaksi.id_transaksi=tb_transaksi.id_transaksi
group by CAST(tb_transaksi.tgl AS DATE) limit 7;
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
FROM tb_transaksi JOIN tb_outlet ON tb_transaksi.id_outlet=tb_outlet.id_outlet JOIN tb_user ON tb_transaksi.id_user=tb_user.id_user JOIN tb_member ON tb_transaksi.id_member=tb_member.id_member
ORDER BY tb_transaksi.id_transaksi ASC;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `transaksiselectbyid` (IN `id_tr` INT)   BEGIN
SELECT * FROM tb_transaksi WHERE id_transaksi=id_tr;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `transaksistatus` ()   BEGIN
SHOW COLUMNS FROM tb_transaksi WHERE FIELD='status';
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `transaksitambah` (IN `id_out_tr` INT, IN `id_user_tr` INT, IN `id_member_tr` INT, IN `tgl_tr` DATE, IN `batas_waktu_tr` DATE, IN `waktu_bayar_tr` DATE, IN `biaya_tambahan_tr` VARCHAR(255), IN `diskon_tr` VARCHAR(255), IN `status_tr` ENUM('baru','proses','selesai','diambil'), IN `dibayar_tr` ENUM('dibayar','belum_dibayar'))   BEGIN
INSERT INTO tb_transaksi(id_outlet, id_user, id_member, tgl, batas_waktu, waktu_bayar, biaya_tambahan, diskon, status, dibayar)
VALUES(id_out_tr, id_user_tr, id_member_tr, tgl_tr, batas_waktu_tr, waktu_bayar_tr, biaya_tambahan_tr, diskon_tr, status_tr, dibayar_tr);
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
(1, 'Kita', 'Jl. Kitaaaan No.1', 'P', '081234567890');

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
(1, 'UKK', 'Jl. UKK.jpg', '081234567890');

-- --------------------------------------------------------

--
-- Table structure for table `tb_paket`
--

CREATE TABLE `tb_paket` (
  `id_paket` int(11) NOT NULL,
  `id_outlet` int(11) DEFAULT NULL,
  `jenis` enum('Kiloan','Selimut','Bed Cover','Kaos','Lain') DEFAULT NULL,
  `nama_paket` varchar(100) DEFAULT NULL,
  `harga` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_paket`
--

INSERT INTO `tb_paket` (`id_paket`, `id_outlet`, `jenis`, `nama_paket`, `harga`) VALUES
(1, 1, 'Bed Cover', 'Turu cover', 50000),
(2, 1, 'Kiloan', 'Kilos', 10000),
(3, 1, 'Selimut', 'Selimute', 20000);

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
  `status` enum('Baru','Proses','Selesai','Diambil') DEFAULT NULL,
  `dibayar` enum('Dibayar','Belum_Dibayar') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Triggers `tb_transaksi`
--
DELIMITER $$
CREATE TRIGGER `kode_invoice` BEFORE INSERT ON `tb_transaksi` FOR EACH ROW BEGIN
    SET NEW.kode_invoice = CONCAT('L-', (SELECT MAX(id_transaksi) + 1 FROM tb_transaksi), '-', DATE(now()));
END
$$
DELIMITER ;
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
  `role` enum('Admin','Kasir','Owner') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_user`
--

INSERT INTO `tb_user` (`id_user`, `id_outlet`, `nama`, `username`, `password`, `role`) VALUES
(1, 1, 'Rei', 'Rei', 'Rei', 'Admin');

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
  MODIFY `id_aksi` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=132;

--
-- AUTO_INCREMENT for table `tb_detail_transaksi`
--
ALTER TABLE `tb_detail_transaksi`
  MODIFY `id_det_transaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `tb_member`
--
ALTER TABLE `tb_member`
  MODIFY `id_member` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tb_outlet`
--
ALTER TABLE `tb_outlet`
  MODIFY `id_outlet` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `tb_paket`
--
ALTER TABLE `tb_paket`
  MODIFY `id_paket` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `tb_transaksi`
--
ALTER TABLE `tb_transaksi`
  MODIFY `id_transaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

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
