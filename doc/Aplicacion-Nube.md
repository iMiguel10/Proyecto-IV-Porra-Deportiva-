## Configuración de Aplicación en la nube
---


Para la configuración del despliegue y despliegue en si se han realizado como 3 partes :

* Provisionamiento.
* Creación de la maquina virtual y despliegue de la misma.
* Despliegue.


### 1. Provisionamiento
---

Para el provisionamiento se ha usado un script de ansible en el que hemos puesto las tareas necesarias que se tienen que llevar a cabo para que la máquina virtual tenga todos los requisitos que hacen falta para que la aplicación funcione correctamente.

Para ello lo primero que ha sido necesario ha sido definir los host en el archivo de host de ansible (*/etc/ansible/hosts*), en el que se ha añadido ( en mi caso ) lo siguiente:

~~~
porradeportiva
porradeportiva.westus.cloudapp.azure.com
~~~

ó

~~~
porradeportiva
104.40.9.222 

~~~

La orden para la ejecución del script fuera del Vagrantfile es `ansible-playbook playbook.yml`.

![Script Ansible](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-1.png)

### 2. Creación de la maquina virtual y despliegue de la misma
---

Para la creación y despliegue de la maquina virtual que contendrá nuestra aplicación se ha usado vagrant para la creación y azure para el despliegue, de manera que ha sido necesario la definición de un Vagrantfile:

~~~

Vagrant.configure('2') do |config|
  config.vm.box = 'azure'

  # use local ssh key to connect to remote vagrant box
  config.ssh.private_key_path = '~/.ssh/id_rsa'
  config.vm.provider :azure do |azure, override|

    # each of the below values will default to use the env vars named as below if not specified explicitly
    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

    azure.vm_name = 'porradeportiva'
    azure.vm_size = 'Standard_B1s'
    azure.tcp_endpoints = '80'

  end

  config.vm.provision :ansible do |ansible|
      ansible.playbook = "provision/playbook.yml"
  end

end

~~~

En este fichero como podemos ver se han usado unas reglas específicas para el uso y despliegue de una máquina virtual con [vagrant y azure](https://github.com/Azure/vagrant-azure), de este fichero podemos comentar que se han tenido que exportar variables de entorno para que las claves e identificadores de la suscripción no sean visibles, además de exportarlas se han añadido al archivo */etc/environments* para que se exporten cada vez que se arranque la máquina anfitriona, como segunda cosa a comentar son los parámetros opcionales como el *name, size, tcp_enpoints* que nos han permitido asignarle el nombre de porradeportiva, tamaño y puertos que vamos a necesitar de la máquina virtual alojada en azure, y por última cosa a comentar es la última parte y es en la que se ejecuta el script de provisionamiento descrito en el punto anterior.

Antes de levantar la máquina virtual es necesario la instalación de un plugin de azure para vagrant.

![Plugin Azure](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-2.png)

Por otro lado, para la obtención de las variables necesarias para el Vagrantfile ha sido necesario el uso del Azure cli, para ello mostramos a continuación con imágenes el logueo, obtención de datos y creación de un directorio activo de azure.

![Login Azure](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-3.png)
![List Azure](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-4.png)
![AD Azure](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-5.png)

Una vez hecho todo lo anterior podemos hacer `vagrant up --provider=azure`.

![Vagrant Up](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-6.png)

Tras este proceso vamos al nuestro portal azure y podemos ver todos los recursos que se han creado automáticamente.

![Portal Azure](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-7.PNG)


### 3. Despliegue
---
Para el despliegue es necesario crear un archivo [**fabfile.py**](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/despliegue/fabfile.py) en nuestro repositorio, que nos permitirá llavar a cabo ordenes de una manera automatizada a través de ssh.

**Mi archivo fabfile.py**  

~~~

# Fabfile to:
#    - Testear
#    - Borrar
#    - Actualizar
#    - Iniciar

import os

# Import Fabric's API module
from fabric.api import *
from fabric.contrib.console import confirm

# Host a los que se conectará
env.hosts = ['porradeportiva.westus.cloudapp.azure.com']

# Usuario usado 
env.user = "vagrant"
env.password = os.environ["PASSWORD"]


def Test():
    with cd("Proyecto-IV-Porra-Deportiva-/test/"):
        result = run("python3 test.py && pytest")
        if result.failed and not confirm("Tests failed. Continue anyway?"):
            abort("TEST fallidos")

def Borrar():

    # Borramos antiguo codigo
    run('rm -rf Proyecto-IV-Porra-Deportiva-')


def Actualizar():

    # Borramos antiguo codigo
    Borrar()

    # Descargaos el repositorio
    run("git clone https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-.git")

    # Instalamos requirements
    run('pip3 install -r Proyecto-IV-Porra-Deportiva-/requirements.txt')

    # Comprobamos que pasa los test
    Test()

def Iniciar():

    # Iniciamos el servicio web
    with cd("Proyecto-IV-Porra-Deportiva-/src/"):
        sudo('gunicorn porradepapp:app -b 0.0.0.0:80 &')

~~~

Como podemos ver tenemos diferentes funciones en las que hemos definido una serie de posibles ordenes que queremos que se ejecuten en nuestra máquina para borrar, actualizar o iniciar nuestra aplicación.

La orden utilizada para realizar alguna de las funciones de despliegue es:  
`fab -f despliegue/fabfile.py -H vagrant@porradeportiva.westus.cloudapp.azure.com <función>`  
Pero en mi caso es `fab -f despliegue/fabfile.py <función>`, ya que hemos añadido esto:

~~~

# Host a los que se conectará
env.hosts = ['porradeportiva.westus.cloudapp.azure.com']

# Usuario usado 
env.user = "vagrant"
env.password = os.environ["PASSWORD"]

~~~

![Fabfile](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-8.png)  
![Fabfile](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-9.png)  
![Fabfile](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-10.png)  
![Fabfile](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-11.png)  

Información obtenida de:  

* [Fabric Doc](http://docs.fabfile.org/en/1.14/tutorial.html)
* [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-use-fabric-to-automate-administration-tasks-and-deployments)
* [Bogotobogo](https://www.bogotobogo.com/python/Fabric/python_Fabric.php)
* [Tutsplus](https://code.tutsplus.com/tutorials/getting-started-with-the-fabric-python-library--cms-30555)
* [Python for Beginners](https://www.pythonforbeginners.com/systems-programming/how-to-use-fabric-in-python)

### 4. Ejemplos
---

Para ver el estado de la máquina podemos acceder a través de:

- **IP pública:** 104.40.9.222
- **DNS:**  porradeportiva.westus.cloudapp.azure.com 

Para ver las rutas activas se puede ver la api que ofrece: [porradepapp.py](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/src/porradepapp.py).