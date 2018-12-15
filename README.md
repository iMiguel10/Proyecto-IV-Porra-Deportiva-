[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)    [![Build Status](https://travis-ci.com/iMiguel10/Proyecto-IV-Porra-Deportiva-.svg?branch=master)](https://travis-ci.com/iMiguel10/Proyecto-IV-Porra-Deportiva-)

# Proyecto IV (Porra Deportiva)
Repositorio para la asignatura de 4º curso, infraestructura virtual (IV), del grado de ingeniería informática (GII) de la universidad de granada (UGR). 

## Descripción

El proyecto consistirá en un microservicio en la nube basado en una porra deportiva, en el que existirán usuarios, resultados, jornadas y enfrentamientos. En el cual el usuario podrá realizar sus predicciones de cualquier partido de cada una de las jornadas que desee.  
El proyecto está pensado como un microservicio que se podría integrar a servicios como aplicaciones de apuestas deportivas.

## Herramientas
  
* Este proyecto será abordado con el lenguaje de programación Python.  
* Se usará el micro-framework Flask para el desarrollo del microservicio, ya que parece ser una buena herramienta para iniciarse en el lenguaje de programación que usaremos.
*  Se usará un entorno virtual para el desarrollo utilizando `virtualenv`.  
* La idea es usar una base de datos, como es MongoDB, para almacenar los distintos elementos que aparecen en nuestra porra (apuestas y jornadas), pero en principio se usará almacenamiento estático en ficheros JSON.  
* Para el desarrollo basado en test se implementarán pruebas unitarias en python del framework incluido en la librería estándar `unittest`.
Se tiene pensado utilizar Travis CI, ya que nos permite pasar los test y además incorporarlo con GitHub.

[**Documentación Herramientas**](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/doc/Info-herramientas.md)

## Integración continua  (Travis-CI)

La clase que se va a testear es [**funcionalidadesbasicasDB.py**](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/src/funcionesbasicasDB.py), esta clase incluye funciones como son ver todos los partidos de una jornada, ver el partido concreto de una jornada concreta, ver las apuestas de un usuario, y añadir un partido a una jornada.  
El uso que tendría esta clase es mostrar y añadir partidos o jornadas completas dentro de la aplicación de apuestas.

Por otro lado para **instalarla y testearla** es necesario instalar los [*requirements.txt*](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/requirements.txt) con *pip* y descargar los archivos de código y almacenamiento ( archivos de la carpeta [src](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/tree/master/src) ), y para testearla basta con ejecutar la clase de test [*test.py*](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/test/test.py) tras la instalación como se puede ver en la documentación del enlace de abajo.

[**Documentación Integración Contínua**](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/doc/Integ-Cont-Conf.md)

## Configuración de un PaaS  (Heroku)


Para hacer que nuestro microservicio comience a funcionar se ha elegido el PasS Heroku.  
Los motivos por los que se ha elegido han sido varios:

* Es gratis.
* Fácil de manejar.
* Permite una rápida puesta en marcha.
* Permite la integración con GitHub y Travis-CLI.

**Despliegue:** https://porra-deportiva.herokuapp.com/ 

[**Documentación PaaS**](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/doc/PaaS-Conf.md)

## Configuración de un entorno de pruebas usando contenedores (Docker + Heroku)

**Contenedor:** https://container-porra-dep.herokuapp.com

Para la creación y uso de este entorno de pruebas, se han usado los contenedores [Docker](https://www.docker.com/), para el despliegue del contenedor se ha usado [Heroku](https://www.heroku.com/), y además la publicación de la imagen en [DockerHub](https://hub.docker.com/).

La URL del despliegue de la imagen en DockerHub es https://hub.docker.com/r/imiguel10/proyecto-iv-porra-deportiva/ .  
El entorno se puede descargar con una sola orden de DockerHub:  `docker run -it imiguel10/proyecto-iv-porra-deportiva`.

[**Documentación Docker**](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/doc/Docker-Conf.md)

## Despliegue desde 0 de una aplicación en la nube.

**Despliegue final:** 104.40.9.222

Para el despliegue de una aplicación en la nube desde 0, en nuestro caso de Azure, se ha hecho, por así decirlo, en 3 partes, provisionamiento ( con ansible ), creación de una máquina virtual ( con vagrant ) y despliegue ( con fabric ).

Para la realización de las tareas anteriores han sido necesarios 3 ficheros: [playbook.yml](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/provision/playbook.yml), [Vagrantfile](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/Vagrantfile) y [fabfile.py](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/despliegue/fabfile.py).

Por otra parte se quiere remarcar que el proyecto consta de funcionalidad para gestionar jornadas y apuestas, y hace uso, como se indica al inicio, de una base de datos Mongo, desplegada en [MongoDB Atlas](https://www.mongodb.com/cloud/atlas?lang=es-es) 

[**Documentación Aplicación en la Nube**](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/doc/Aplicacion-Nube.md)