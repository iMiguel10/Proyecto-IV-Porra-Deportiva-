## Configuración de un PaaS  (Heroku)
---

Para hacer el despliegue en [Heroku](https://www.heroku.com/) el PaaS elegido ha sido necesario:

### 1. Registrarse en [Heroku](https://www.heroku.com/)

**Nota:** Para poner correctamente el botón de [Heroku](https://www.heroku.com/) ha sido necesario crear un archivo  [app.json](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/app.json) con datos de la aplicación.


---

### 2. Crear la App
---
Una vez logueados en [Heroku](https://www.heroku.com/) creamos una nueva app, con el nombre que deseemos, en mi caso ha sido **porra-deportiva**.

![Crear App](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/Heroku-1.PNG)

### 3. Crear Procfile
---
Para el despliegue es necesario crear un archivo que se llame **Procfile** en nuestro repositorio, este fichero especifica los comandos que se ejecutan por la aplicación de Dynos.

>> // Mi Archivo Procfile  
>> web: cd src && gunicorn porra-dep-app:app --log-file -  

**NOTA:** Es necesario instalar gnunicorn -- `pip install gunicorn`.  
**NOTA:** Información de [Gunicorn](https://www.pythoniza.me/gunicorn/)

### 4. Asociar GitHub con Heroku + Despliegue Automático
---
* Creada ya, vamos a Deploy.
* En Deployment method seleccionamos GitHub.
* Conectamos con el repositorio donde se encuentre nuestro microservicio.
* Activamos Automatic deploys y marcamos la casilla de que espere a CI para el despliegue. 

![Conf. App](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/Heroku-2.PNG)

### 5. Hacer el primer despliegue
---

Para hacer el primer despliegue sin salirnos de Deploy y con lo anterior realizado le damos a **Deploy Branch.**

Y si todo ha salido bien ya podemos hacer una petición.  
También podemos ver que tenemos la aplicación en la línea de comandos si tenemos el cliente de heroku instalado y nos logueamos.

![Heroku App](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/Heroku-3.PNG)

### 6. Ejemplos
---

https://porra-deportiva.herokuapp.com/  --> Status: OK.  
https://porra-deportiva.herokuapp.com/jornada/1 --> Devuelve los partidos de la jornada 1.   
https://porra-deportiva.herokuapp.com/partido/2/jornada/1 --> Devuelve el partido 2 de la jornada 1.  
https://porra-deportiva.herokuapp.com/apuesta/luis14 --> Devuelve las apuestas del usuario luis14

**NOTA:** Si cambias los números cambian la jornada o el partido.   
**NOTA:** Si cambias luis14 por otro usuario que tenga apuestas también cambian. 
 


