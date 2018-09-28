[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

# Proyecto IV (Porra Deportiva)
Repositorio para la asignatura de 4º curso, infraestructura virtual (IV), del grado de ingeniería informática (GII) de la universidad de granada (UGR). 

## Descripción

El proyecto consistirá en un microservicio en la nube basado en una porra deportiva, en el que existirán usuarios, resultados, jornadas y enfrentamientos. En el cual el usuario podrá realizar sus predicciones de cualquier partido de cada una de las jornadas que desee.  
El proyecto está pensado como un microservicio que se podría integrar a servicios como aplicaciones de apuestas deportivas.

## Herramientas
  
Este proyecto será abordado con el lenguaje de programación Python.  
Se usará un entorno virtual para el desarrollo utilizando `virtualenv`.  
La idea es usar una base de datos para almacenar los distintos elementos que aparecen en nuestra porra (usuarios, resultados, jornadas ... ).  
Para el desarrollo basado en test se implementarán pruebas unitarias en python del framework incluido en la librería estándar `unittest`.
Se tiene pensado utilizar Travis CI, ya que nos permite pasar los test y además incorporarlo con GitHub.