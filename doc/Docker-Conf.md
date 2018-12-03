## Configuración de Docker
---


Para la configuración del entorno de pruebas se han llevado a cabo varias tareas:

* Instalación de Docker
* Creación del Dockerfile
* Despliegue de la aplicación en Heroku en el contenedor Docker
* Publicación de la imagen Docker en DokerHub.




### 1. Instalación de Docker

---

Para la instalación de Docker se ha seguido el siguiente [tutorial](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce) que viene en la documentación oficial.


### 2. Crear del Dockerfile 

---
Para la creación de nuestro [Dockerfile](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/Dockerfile) se ha usado una [imagen de Python](https://hub.docker.com/_/python/) y se ha obtenido información de las siguientes páginas: [StackOverflow](https://stackoverflow.com/questions/43925487/how-to-run-gunicorn-on-docker) y [Colaboratorio](https://colaboratorio.net/davidochobits/sysadmin/2018/crear-imagenes-medida-docker-dockerfile/).

El contenido de nuestro Dockerfile es el siguiente:

~~~

FROM python:3

MAINTAINER Miguel imiguel10@correo.ugr.es

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/

WORKDIR src/

EXPOSE 80

CMD ["gunicorn", "-b", "0.0.0.0:80", "porra-dep-app:app"]

~~~

En el podemos ver:  

+ **FROM:** Imagen usada por nuestro contenedor, en nuestro caso una de Python 3, ya que nuestro servicio está desarrollado en Python, y además se ha elegido esa imagen porque, a pesar de ser grande, es la única que proporciona todos los requisitos para la instalación de mis requirements.
+ **MAINTAINER:** Datos del desarrollador del contenedor, en este caso los mios.
+ **COPY:** En el primero copiamos el requirements para a continuación instalarlo, y en el segundo se copian los archivos de código del servicio, que están alojados en la carpeta src/.
+ **RUN:** Comando que ejecuta el contenedor al compilarlo, que aquí usaremos para instalar nuestros requirements.
+ **WORKDIR:** Comando que nos situará en el directorio de trabajo dentro del contenedor, en mi caso me llevará a la carpeta src que es dónde están alojados los archivos del servicio.
+ **EXPOSE:** Asigna el puerto que usará el contenedor, en nuestro caso al ser un servicio web le asignaremos el puerto 80.
+ **CMD:** Comando que se ejecutará cuando empiece a correr nuestra imagen, que es el mismo que se ha usado en heroku.yml para el despliegue del contenedor y en el procfile para el despliegue de la aplicación, ambos en Heroku.

**Ordenes usadas en local para la compilación y ejecución:**  
`docker build -t my-python-app .`  # Compilación.  
`docker run -it --rm --name my-running-app -p 8080:80 my-python-app` # Ejecución de la imagen compilada.


### 3. Despliegue de la aplicación en Heroku en el contenedor Docker
---
Para el despliegue es necesario crear un archivo **heroku.yml** en nuestro repositorio, que nos permitirá que [Heroku](https://www.heroku.com/) cree la imagen a partir del Dockerfile y ejecute la orden necesaria para que el servicio web se ponga en fucnionamiento.

**Mi archivo [heroku.yml](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/heroku.yml)**  

~~~

build:
  docker:
    web: Dockerfile
run:
  web: gunicorn porra-dep-app:app 

~~~

Aquí podemos ver que tenemos 2 partes, la primara para que Heroku compile la imagen a partir del Dockerfile, y la segunda es el comando o acción que ejecutará para poner en funcionamiento el servicio web.

**NOTA:** Información obtenida a partir de la [documentación de Heroku.](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml)  
**NOTA:** En este apartado también se ha activado la opción de despliegue automático a partir de GitHub.

### 4. Publicación de la imagen Docker en DokerHub.
---

Para la publicación de la imagen en DockerHub se ha creado una compilación automática a partir de este repositorio de GitHub, de manera que si se hiciese algún cambio en el Dockerfile la imagen quede actualizada automáticamente.

![DockerHub](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/DockerHub-Auto.PNG)

[Imagen en DockerHub](https://hub.docker.com/r/imiguel10/proyecto-iv-porra-deportiva/)

Para la utilización directa de la imagen, solo es necesario hacer: `docker run -it imiguel10/proyecto-iv-porra-deportiva`.

![DockerHub](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/DockerHub.PNG)

### 5. Ejemplos
---

https://container-porra-dep.herokuapp.com/  --> Status: OK.  
https://container-porra-dep.herokuapp.com/status  --> Status: OK.  
https://container-porra-dep.herokuapp.com/jornada/1 --> Devuelve los partidos de la jornada 1.   
https://container-porra-dep.herokuapp.com/partido/2/jornada/1 --> Devuelve el partido 2 de la jornada 1.  
https://container-porra-dep.herokuapp.com/apuesta/luis14 --> Devuelve las apuestas del usuario luis14

**NOTA:** Si cambias los números cambian la jornada o el partido.   
**NOTA:** Si cambias luis14 por otro usuario que tenga apuestas también cambian. 