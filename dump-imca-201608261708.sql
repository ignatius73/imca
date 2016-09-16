-- MySQL dump 10.16  Distrib 10.1.16-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: imca
-- ------------------------------------------------------
-- Server version	10.1.16-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alumnos`
--

DROP TABLE IF EXISTS `alumnos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alumnos` (
  `idAlumnos` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(255) DEFAULT NULL,
  `Apellido` varchar(255) DEFAULT NULL,
  `DNI` bigint(20) NOT NULL,
  `Nacionalidad` int(10) unsigned DEFAULT NULL,
  `Fecha_Nacimiento` date DEFAULT NULL,
  `Edad` int(10) unsigned DEFAULT NULL,
  `Domicilio` varchar(255) DEFAULT NULL,
  `Localidad` varchar(255) NOT NULL,
  `Partido` varchar(255) NOT NULL,
  `CP` varchar(30) DEFAULT NULL,
  `Telefono` int(10) unsigned DEFAULT NULL,
  `Celular` int(10) unsigned DEFAULT NULL,
  `Estudios_Cursados` int(10) unsigned DEFAULT NULL,
  `Otros` varchar(255) DEFAULT NULL,
  `Trabaja` tinyint(1) DEFAULT NULL,
  `Ocupacion` varchar(255) DEFAULT NULL,
  `Grupo_Sanguineo` varchar(45) DEFAULT NULL,
  `Antitetanica` tinyint(1) DEFAULT NULL,
  `Presion_Arterial` float DEFAULT NULL,
  `Enfermedades` varchar(255) DEFAULT NULL,
  `Tratamiento` tinyint(1) DEFAULT NULL,
  `alergias` varchar(255) DEFAULT NULL,
  `emergencias` varchar(255) DEFAULT NULL,
  `osocial` varchar(255) DEFAULT NULL,
  `foto` blob,
  `Sexo` varchar(100) DEFAULT NULL,
  `Carrera` varchar(255) DEFAULT NULL,
  `ciclo` date DEFAULT NULL,
  `cohorte` date DEFAULT NULL,
  `Lugar_Nacimiento` varchar(255) DEFAULT NULL,
  `Estado_Civil` varchar(100) DEFAULT NULL,
  `hijos` tinyint(3) unsigned DEFAULT NULL,
  `acargo` varchar(255) DEFAULT NULL,
  `numero` int(10) unsigned DEFAULT NULL,
  `piso` varchar(3) DEFAULT NULL,
  `depto` varchar(5) DEFAULT NULL,
  `mail` varchar(100) DEFAULT NULL,
  `egreso` date DEFAULT NULL,
  `insti_otros` text,
  `escuela` varchar(255) DEFAULT NULL,
  `distrito` tinyint(3) unsigned DEFAULT NULL,
  `doc_dni` tinyint(1) DEFAULT NULL,
  `doc_Tit` tinyint(1) DEFAULT NULL,
  `doc_Reg` tinyint(1) DEFAULT NULL,
  `doc_fot` tinyint(1) DEFAULT NULL,
  `doc_cert` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`idAlumnos`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumnos`
--

LOCK TABLES `alumnos` WRITE;
/*!40000 ALTER TABLE `alumnos` DISABLE KEYS */;
/*!40000 ALTER TABLE `alumnos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asignaturas`
--

DROP TABLE IF EXISTS `asignaturas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asignaturas` (
  `id_asignatura` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `carrera` varchar(255) NOT NULL,
  `correlativas` text COMMENT 'igual a id_asignaturas',
  `horario` text,
  `vacantes` text,
  `anio` tinyint(4) DEFAULT NULL,
  `cursada_paralela` int(11) DEFAULT NULL COMMENT 'igual a id_asignatura',
  PRIMARY KEY (`id_asignatura`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asignaturas`
--

LOCK TABLES `asignaturas` WRITE;
/*!40000 ALTER TABLE `asignaturas` DISABLE KEYS */;
INSERT INTO `asignaturas` VALUES (1,'DIBUJO','1',NULL,NULL,NULL,0,NULL),(2,'PINTURA (TECNOLOGÍA)','1',NULL,NULL,NULL,0,NULL),(3,'ESCULTURA CERAMICA (MODELADO)','1',NULL,NULL,NULL,0,NULL),(4,'ARTES DEL FUEGO I (DECORACIÓN)','1',NULL,NULL,NULL,0,NULL),(5,'ARTES DEL FUEGO II (ALFARERÍA)','1',NULL,NULL,NULL,0,NULL),(6,'LENGUAJE VISUAL','1',NULL,NULL,NULL,0,NULL),(7,'HISTORIA DEL ARTE Y LA CULTURA','1',NULL,NULL,NULL,0,NULL),(8,'INTRODUCCIÓN AL ANÁLISIS','1',NULL,NULL,NULL,0,NULL),(9,'DIBUJO I','5',NULL,NULL,NULL,1,NULL),(10,'QUÍMICA APLICADA I','5',NULL,NULL,NULL,1,NULL),(11,'ALFARERÍA','2',NULL,NULL,NULL,1,NULL),(12,'MOLDERÍA I','2',NULL,NULL,NULL,1,NULL),(13,'LENGUAJE VISUAL I','5',NULL,NULL,NULL,1,NULL),(14,'HISTORIA DEL ARTE I/HISTORIA DE LAS ARTES VISUALES','5',NULL,NULL,NULL,1,NULL),(15,'CERÁMICA (MODELADO/DECORACIÓN)','2',NULL,NULL,NULL,1,NULL),(16,'PROYECTO Y DISEÑO CERÁMICO I/DIBUJO II','5','9,13',NULL,NULL,2,NULL),(17,'TECNOLOGÍA APLICADA A LA CERÁMICA I','5','29,10',NULL,NULL,2,NULL),(18,'MOLDERÍA II','2',NULL,NULL,NULL,2,NULL),(19,'LENGUAJE VISUAL II','5','13',NULL,NULL,2,NULL),(20,'TEORÍA DE LA PERCEPCIÓN Y LA COMUNICACIÓN','2',NULL,NULL,NULL,2,NULL),(21,'HISTORIA DEL ARTE II/HISTORIA DE LAS ARTES VISUALES II','5','14',NULL,NULL,2,NULL),(22,'CERÁMICA Y ALFARERÍA(DECORACIÓN/ALFARERÍA/MODELADO) ','2',NULL,NULL,NULL,2,NULL),(23,'PROYECTO Y DISEÑO CERÁMICO II/DIBUJO III','5','16,19',NULL,NULL,3,NULL),(24,'TECNOLOGÍA APLICADA A LA CERÁMICA II','2',NULL,NULL,NULL,3,NULL),(25,'ARTES, CULTURAS Y ESTÉTICAS EN EL MUNDO CONTEMPORÁNEO (MODELADO)','2',NULL,NULL,NULL,3,NULL),(26,'HISTORIA DE LA CERÁMICA Y PROYECTO DE ANÁLISIS','2',NULL,NULL,NULL,3,NULL),(27,'ESPACIO INSTITUCIONAL (LENGUAJE VISUAL)','2',NULL,NULL,NULL,3,NULL),(28,'CERÁMICA-MOLDERÍA-ALFARERÍA (MODELADO/MATRICERÍA/ALFARERÍA)/CERÁMICA III','5','35,17,19,16',NULL,NULL,3,NULL),(29,'CERÁMICA I (ALFARERÍA/MOLDERÍA/DECORACIÓN)','3',NULL,NULL,NULL,1,NULL),(30,'TALLER COMPLEMENTARIO (ESCULTURA/MODELADO)','3',NULL,NULL,NULL,1,NULL),(31,'PRÁCTICA DOCENTE I','3',NULL,NULL,NULL,1,NULL),(32,'PSICOLOGÍA DE LA EDUCACIÓN I','3',NULL,NULL,NULL,1,NULL),(33,'FUNDAMENTOS DE LA EDUCACIÓN','3',NULL,NULL,NULL,1,NULL),(34,'HISTORIA SOCIAL GENERAL','3',NULL,NULL,NULL,1,NULL),(35,'CERÁMICA II (DECORACIÓN/ALFARERÍA)','3','29,10,13,9',NULL,NULL,2,NULL),(36,'TALLER COMPLEMENTARIO II (ESCULTURA/MODELADO)','3','30,9,13',NULL,NULL,2,NULL),(37,'PRÁCTICA DOCENTE II','3','31,33,32',NULL,NULL,2,NULL),(38,'HISTORIA SOCIOPOLÍTICA DE LATINOAMÉRICA Y ARGENTINA','3','34',NULL,NULL,2,NULL),(39,'DIDÁCTICA GENERAL','3','33,32',NULL,NULL,2,NULL),(40,'PSICOLOGÍA DE LA EDUCACIÓN II','3','33,32',NULL,NULL,2,NULL),(41,'LENGUAJE VISUAL III','3','19',NULL,NULL,3,NULL),(42,'DIDÁCTICA DE LAS ARTES VISUALES I','3','39,40,37',NULL,NULL,3,NULL),(43,'QUÍMICA APLICADA II','3','17,35',NULL,NULL,3,NULL),(44,'MEDIOS AUDIOVISUALES E IMAGEN DIGITAL','3','19,16',NULL,NULL,3,NULL),(45,'HISTORIAS DE LAS ARTES VISUALES III','3','21',NULL,NULL,3,NULL),(46,'PRÁCTICA DOCENTE III','3','19,16,35,17,36,21,37,38,39,40',NULL,NULL,3,42),(47,'POLÍTICA EDUCATIVA','3','39,38',NULL,NULL,3,NULL),(48,'TEORÍAS DEL ARTE I','3','38,21',NULL,NULL,3,NULL),(49,'CERÁMICA IV','3','42,41,23',NULL,NULL,4,NULL),(50,'DIBUJO IV','3','41,23',NULL,NULL,4,NULL),(51,'ARTES COMBINADAS','3','23,16,36',NULL,NULL,4,NULL),(52,'DIDÁCTICA DE LAS ARTES VISUALES II','3','42,47',NULL,NULL,4,NULL),(53,'PRÁCTICA DOCENTE IV','3','41,23,28,43,44,45,42,46,47,48',NULL,NULL,4,52),(54,'TEORÍAS DEL ARTE II','3','48,45',NULL,NULL,4,NULL),(55,'METODOLOGÍA DE LA INVESTIGACIÓN','3','48,45',NULL,NULL,4,NULL);
/*!40000 ALTER TABLE `asignaturas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `calificaciones`
--

DROP TABLE IF EXISTS `calificaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `calificaciones` (
  `id_calif` int(11) NOT NULL AUTO_INCREMENT,
  `id_asign` int(11) NOT NULL,
  `cuatri1` int(11) NOT NULL,
  `cuatri2` int(11) NOT NULL,
  `recup` int(11) DEFAULT NULL,
  `final1` int(11) NOT NULL,
  `final2` int(11) DEFAULT NULL,
  `final3` int(11) DEFAULT NULL,
  `final4` int(11) DEFAULT NULL,
  `nota` int(11) DEFAULT NULL,
  `fecha_final` date NOT NULL,
  PRIMARY KEY (`id_calif`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calificaciones`
--

LOCK TABLES `calificaciones` WRITE;
/*!40000 ALTER TABLE `calificaciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `calificaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carreras`
--

DROP TABLE IF EXISTS `carreras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `carreras` (
  `id_carrera` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_carrera`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carreras`
--

LOCK TABLES `carreras` WRITE;
/*!40000 ALTER TABLE `carreras` DISABLE KEYS */;
INSERT INTO `carreras` VALUES (1,'FOBA'),(2,'TECNICATURA'),(3,'LICENCIATURA EN ARTES VISUALES'),(4,'CURSOS EXTRAPROGRAMATICOS'),(5,'AMBAS');
/*!40000 ALTER TABLE `carreras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'imca'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-08-26 17:08:43