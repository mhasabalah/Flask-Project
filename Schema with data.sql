CREATE DATABASE  IF NOT EXISTS `health_insurance` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `health_insurance`;
-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: health_insurance
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `claims`
--

DROP TABLE IF EXISTS `claims`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `claims` (
  `claims_Id` int NOT NULL AUTO_INCREMENT,
  `Cost` int NOT NULL,
  `Description` varchar(200) NOT NULL,
  `Hospital_id` int NOT NULL,
  `Customer_Id` int NOT NULL,
  `Dependant_ID` int DEFAULT NULL,
  `Status` tinyint DEFAULT NULL,
  PRIMARY KEY (`claims_Id`),
  KEY `fk_Claims_Hospitals1_idx` (`Hospital_id`),
  KEY `fk_Claims_Customers1_idx` (`Customer_Id`),
  KEY `fk_Claims_Dependants1_idx` (`Dependant_ID`),
  CONSTRAINT `fk_Claims_Customers1` FOREIGN KEY (`Customer_Id`) REFERENCES `customers` (`Customer_Id`),
  CONSTRAINT `fk_Claims_Dependants1` FOREIGN KEY (`Dependant_ID`) REFERENCES `dependants` (`Dep_ID`),
  CONSTRAINT `fk_Claims_Hospitals1` FOREIGN KEY (`Hospital_id`) REFERENCES `hospitals` (`Hospital_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `claims`
--

LOCK TABLES `claims` WRITE;
/*!40000 ALTER TABLE `claims` DISABLE KEYS */;
INSERT INTO `claims` VALUES (1,700,'x-ray',1,1,NULL,0),(2,1000,'surgery',2,1,2,1),(3,850,'x-ray',1,2,3,0),(4,1000,'broken hand needs surgery',2,16,4,0),(5,1000,'broken heart',2,9,NULL,0);
/*!40000 ALTER TABLE `claims` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `Customer_Id` int NOT NULL AUTO_INCREMENT,
  `Customer_Name` varchar(45) NOT NULL,
  `DateOfBirth` date NOT NULL,
  `City` varchar(45) NOT NULL,
  `Street` varchar(45) DEFAULT NULL,
  `Building_Number` varchar(45) DEFAULT NULL,
  `PhoneNumber` varchar(45) NOT NULL,
  `Beneficiary_Plan` int DEFAULT NULL,
  PRIMARY KEY (`Customer_Id`),
  UNIQUE KEY `PhoneNumber` (`PhoneNumber`),
  UNIQUE KEY `Beneficiary_Plan` (`Beneficiary_Plan`),
  KEY `fk_Customers_Purchasd Plans1_idx` (`Beneficiary_Plan`),
  CONSTRAINT `fk_Customers_Purchasd Plans1` FOREIGN KEY (`Beneficiary_Plan`) REFERENCES `purchasd plans` (`PurchasedPlanID`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'belal','2000-05-08','tanta','aboTaleb','14','01258963574',1),(2,'diaa','2000-05-08','cairo','saeed','10','01296358742',3),(3,'adnan','2000-12-07','alex','naser','8','01285963745',NULL),(4,'ali','2006-01-22','tanta','helw','6','01258743652',NULL),(5,'ali','2007-01-22','giza','kasr','7','01258743692',NULL),(9,'بلال','2022-01-11','tanta','1ِِ4th Abo Taleb','none','01288560907',11),(11,'SALAH','2022-01-06','SHARM','ABO TALEB','','05555',NULL),(12,'kady','2001-01-02','SHARM','ahmed metwally','','01258963254',NULL),(14,'SALAHianoh','2021-12-31','SHARM','ABO TALEB','','556656556',NULL),(16,'salma','2000-03-04','cairo','178 naser st','','01258963547',7),(28,'salma','2000-10-28','sale','al wahda','16','777724929',NULL),(29,'shimaa eltaiby','1992-05-08','tanta','14 hamed abd rabuh al galaa','','01019649889',NULL),(31,'hamo','1999-12-18','Tanta','Ali bek','2 elmrakby','01276849876',13);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dependants`
--

DROP TABLE IF EXISTS `dependants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dependants` (
  `Dep_ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `DateOfBirth` date NOT NULL,
  `RelationShip` varchar(45) NOT NULL,
  `Beneficiary_plan` int NOT NULL,
  `Customer_Id` int NOT NULL,
  PRIMARY KEY (`Dep_ID`),
  KEY `fk_Dependants_Purchasd Plans1_idx` (`Beneficiary_plan`),
  KEY `fk_Dependants_Customers1_idx` (`Customer_Id`),
  CONSTRAINT `fk_Dependants_Customers1` FOREIGN KEY (`Customer_Id`) REFERENCES `customers` (`Customer_Id`),
  CONSTRAINT `fk_Dependants_Purchasd Plans1` FOREIGN KEY (`Beneficiary_plan`) REFERENCES `purchasd plans` (`PurchasedPlanID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dependants`
--

LOCK TABLES `dependants` WRITE;
/*!40000 ALTER TABLE `dependants` DISABLE KEYS */;
INSERT INTO `dependants` VALUES (1,'eman','1960-09-28','mother',1,1),(2,'mohammed','1960-08-08','father',2,1),(3,'sameh','2001-09-08','brother',3,2),(4,'ali','1960-04-05','father',8,16),(5,'eman','1965-09-24','mother',10,9),(6,'amro','1985-01-02','husband',12,29);
/*!40000 ALTER TABLE `dependants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enrolled`
--

DROP TABLE IF EXISTS `enrolled`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enrolled` (
  `Hospital_id` int NOT NULL,
  `Plan_Id` int NOT NULL,
  PRIMARY KEY (`Hospital_id`,`Plan_Id`),
  KEY `fk_Hospitals_has_Plans_Plans1_idx` (`Plan_Id`),
  KEY `fk_Hospitals_has_Plans_Hospitals1_idx` (`Hospital_id`),
  CONSTRAINT `fk_Hospitals_has_Plans_Hospitals1` FOREIGN KEY (`Hospital_id`) REFERENCES `hospitals` (`Hospital_id`),
  CONSTRAINT `fk_Hospitals_has_Plans_Plans1` FOREIGN KEY (`Plan_Id`) REFERENCES `plans` (`Plan_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enrolled`
--

LOCK TABLES `enrolled` WRITE;
/*!40000 ALTER TABLE `enrolled` DISABLE KEYS */;
INSERT INTO `enrolled` VALUES (1,1),(6,1),(1,2),(2,2),(6,2),(2,3);
/*!40000 ALTER TABLE `enrolled` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hospitals`
--

DROP TABLE IF EXISTS `hospitals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hospitals` (
  `Hospital_id` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `City` varchar(45) NOT NULL,
  `Street` varchar(45) NOT NULL,
  `Phone` varchar(45) NOT NULL,
  PRIMARY KEY (`Hospital_id`),
  UNIQUE KEY `Name` (`Name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hospitals`
--

LOCK TABLES `hospitals` WRITE;
/*!40000 ALTER TABLE `hospitals` DISABLE KEYS */;
INSERT INTO `hospitals` VALUES (1,'delat','tanat','saeed','01258745963'),(2,'american','cairo','saeed','01258796352'),(3,'delta','sharm','naser','01369524783'),(4,'naser','cairo','slah salem','01258963857'),(6,'hayat','tanta','abo taleb','01258963542');
/*!40000 ALTER TABLE `hospitals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plans`
--

DROP TABLE IF EXISTS `plans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plans` (
  `Plan_Id` int NOT NULL AUTO_INCREMENT,
  `Type` varchar(45) DEFAULT NULL,
  `Price` int NOT NULL,
  PRIMARY KEY (`Plan_Id`),
  UNIQUE KEY `Type_UNIQUE` (`Type`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plans`
--

LOCK TABLES `plans` WRITE;
/*!40000 ALTER TABLE `plans` DISABLE KEYS */;
INSERT INTO `plans` VALUES (1,'basic',10000),(2,'primium',20000),(3,'golden',30000);
/*!40000 ALTER TABLE `plans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchasd plans`
--

DROP TABLE IF EXISTS `purchasd plans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchasd plans` (
  `Customer_Id` int NOT NULL,
  `Plan_Id` int NOT NULL,
  `PurchasedPlanID` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`PurchasedPlanID`),
  KEY `fk_Customers_has_Plans_Plans1_idx` (`Plan_Id`),
  KEY `fk_Customers_has_Plans_Customers1_idx` (`Customer_Id`),
  CONSTRAINT `fk_Customers_has_Plans_Customers1` FOREIGN KEY (`Customer_Id`) REFERENCES `customers` (`Customer_Id`),
  CONSTRAINT `fk_Customers_has_Plans_Plans1` FOREIGN KEY (`Plan_Id`) REFERENCES `plans` (`Plan_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchasd plans`
--

LOCK TABLES `purchasd plans` WRITE;
/*!40000 ALTER TABLE `purchasd plans` DISABLE KEYS */;
INSERT INTO `purchasd plans` VALUES (1,1,1),(1,2,2),(2,1,3),(2,3,4),(1,1,5),(1,1,6),(16,1,7),(16,3,8),(9,1,9),(9,2,10),(9,3,11),(29,1,12),(31,1,13);
/*!40000 ALTER TABLE `purchasd plans` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-07 21:58:14
