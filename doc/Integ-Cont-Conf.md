# Integración Continua (Travis-CI)
---

Para añadir integración continua a nuestro proyecto vamos a utilizar Travis-CI, así que, para ello voy a hacer una explicación para su configuración :

### Paso 1 :
Tener el código con las funcionalidades y los test en el repositorio.

### Paso 2 :
Luego tenemos que vincular nuestra cuenta de GitHub a Travis, para ello basta con ir a la [página de Travis](https://travis-ci.com/).

### Paso 3 :
A continuación debemos seleccionar los repositorios que queremos que Travis pase los test.

### Paso 4 :
Para que Travis funcione correctamente es necesario añadir al repositorio un archivo de configuración *.travil.yml*:
>> language: python
>>
>> python:
>>   - "3.6.6"
>>
>>install:
>>  - pip install -r requirements.txt
>>
>> script:
>>  - make test

### Ejemplo:
![Ejemplo Travis]()
