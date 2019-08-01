-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-07-2019 a las 13:24:55
-- Versión del servidor: 10.3.16-MariaDB
-- Versión de PHP: 7.3.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `u`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiante`
--

CREATE TABLE `estudiante` (
  `usuarioestudiante` varchar(25) NOT NULL,
  `IdEstudiante` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `estudiante`
--

INSERT INTO `estudiante` (`usuarioestudiante`, `IdEstudiante`) VALUES
('Gabriel', '12345'),
('Samanta', '2345'),
('elena', '9874');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `notas`
--

CREATE TABLE `notas` (
  `Idestudiante` varchar(25) NOT NULL,
  `numerolista` int(2) NOT NULL,
  `fisica` int(2) NOT NULL,
  `matematica` int(2) NOT NULL,
  `lenguaje` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `notas`
--

INSERT INTO `notas` (`Idestudiante`, `numerolista`, `fisica`, `matematica`, `lenguaje`) VALUES
('12345', 1, 10, 20, 20),
('2345', 10, 5, 15, 20),
('9874', 16, 18, 20, 19);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `notasfinales`
--

CREATE TABLE `notasfinales` (
  `numerolista` int(2) NOT NULL,
  `fisica` int(2) NOT NULL,
  `matematica` int(2) NOT NULL,
  `lenguaje` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesor`
--

CREATE TABLE `profesor` (
  `IdProfesor` varchar(25) NOT NULL,
  `id` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `profesor`
--

INSERT INTO `profesor` (`IdProfesor`, `id`) VALUES
('DAVID', '1724358518');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `estudiante`
--
ALTER TABLE `estudiante`
  ADD PRIMARY KEY (`IdEstudiante`);

--
-- Indices de la tabla `notas`
--
ALTER TABLE `notas`
  ADD PRIMARY KEY (`numerolista`),
  ADD UNIQUE KEY `Idestudiante` (`Idestudiante`);

--
-- Indices de la tabla `notasfinales`
--
ALTER TABLE `notasfinales`
  ADD UNIQUE KEY `numerolista` (`numerolista`);

--
-- Indices de la tabla `profesor`
--
ALTER TABLE `profesor`
  ADD PRIMARY KEY (`id`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `notas`
--
ALTER TABLE `notas`
  ADD CONSTRAINT `notas_ibfk_1` FOREIGN KEY (`Idestudiante`) REFERENCES `estudiante` (`IdEstudiante`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `notasfinales`
--
ALTER TABLE `notasfinales`
  ADD CONSTRAINT `notasfinales_ibfk_1` FOREIGN KEY (`numerolista`) REFERENCES `notas` (`numerolista`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
