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
40.78.6.136 

~~~

[Provisionamiento](https://www.vagrantup.com/intro/getting-started/provisioning.html)

La orden para la ejecución del script con vagrant es `vagrant provision`.  
La orden para la ejecución del script fuera del Vagrantfile es `ansible-playbook playbook.yml`.

![Script Ansible](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-1.png)

### 2. Creación de la maquina virtual y despliegue de la misma
---

Antes de hacer nada es necesario la instalación de un plugin de azure para vagrant, y además añadir la dummy box, esto nos proporcionará una base para nuestra máquina, en nuestro caso será del [proveedor](https://www.vagrantup.com/intro/getting-started/providers.html) azure.

![Plugin Azure](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-2.png)
![Dummy Azure](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-12.png)


Para la creación y despliegue de la maquina virtual que contendrá nuestra aplicación se ha usado vagrant para la creación y azure para el despliegue, de manera que ha sido necesario la definición de un Vagrantfile, que se ha creado con la siguiente instrucción, `vagrant init vmazure`, tras la adición de la box, ya que es necesario pasarle el nombre que le asignamos al añadirla:

```ruby

# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "vmazure"

  # Usamos las claves privadas locales para conectarnos por ssh a la máquina
  config.ssh.private_key_path = '~/.ssh/id_rsa'

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  config.vm.provider :azure do |vmazure, override|

    # Parámetros de nuestra suscripción necesarios para la creación de la máquina en azure
    vmazure.tenant_id = ENV['AZURE_TENANT_ID']
    vmazure.client_id = ENV['AZURE_CLIENT_ID']
    vmazure.client_secret = ENV['AZURE_CLIENT_SECRET']
    vmazure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

    # Parámteros específicos de la máquina
    # Asiganamos el nombre de 'porradeportiva' a la máquina virtual
    vmazure.vm_name = 'porradeportiva'
    # Asiganamos el tipo de almacenamiento más básico a la máquina, para nuestro servicio no es necesario uno mayor.  
    vmazure.vm_size = 'Standard_B1s'
    # Especificamos los puertos que vamos a usar, en nuestro caso solo será necesario el 80.
    vmazure.tcp_endpoints = '80'
    # Especificamos la imagen que tendremos en nuestra vm. Se ha elegido esta imagen porque las pruebas del 
    # servicio se han hecho sobre Ubuntu y la última versión del 16 porque es de las pocas que nos ofrece azure para este SO.
    vmazure.vm_image_urn = 'canonical:ubuntuserver:16.04-LTS:latest'
    # Especificamos la localización de nuestra máquina.
    vmazure.location = 'westus'
  end

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL

  # Provisionamiento con Ansible
  config.vm.provision :ansible do |ansible|

      ansible.playbook = "provision/playbook.yml"

  end

end

```
Para la creación de este fichero ha sido necesario añadir la configuración de los parámetros de nuestro proveedor, en nuestro caso, azure.
En primer lugar se han añadidos los referentes a la suscripción.
~~~
vmazure.tenant_id = ENV['AZURE_TENANT_ID']
vmazure.client_id = ENV['AZURE_CLIENT_ID']
vmazure.client_secret = ENV['AZURE_CLIENT_SECRET']
vmazure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']
~~~

Para la obtención de estas variables ha sido necesario el uso del Azure cli, para ello mostramos a continuación con imágenes el logueo, obtención de datos y creación de un directorio activo de azure.

![Login Azure](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-3.png)
![List Azure](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-4.png)
![AD Azure](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-5.png)

En segundo lugar se han añadido los referentes a los parámetros específicos a la vm.
~~~

# Asiganamos el nombre de 'porradeportiva' a la máquina virtual
vmazure.vm_name = 'porradeportiva'

# Asiganamos el tipo de almacenamiento más básico a la máquina, para nuestro servicio no es necesario uno mayor.  
vmazure.vm_size = 'Standard_B1s'

# Especificamos los puertos que vamos a usar, en nuestro caso solo será necesario el 80.
vmazure.tcp_endpoints = '80'

# Especificamos la imagen que tendremos en nuestra vm. Se ha elegido esta imagen porque las pruebas del 
# servicio se han hecho sobre Ubuntu y la última versión del 16 porque es de las pocas que nos ofrece azure para este SO.
vmazure.vm_image_urn = 'canonical:ubuntuserver:16.04-LTS:latest'

# Especificamos la localización de nuestra máquina.
vmazure.location = 'westus'

~~~

Las imágenes que nos ofrece azure son: [Selección de imágenes para máquinas virtuales](https://docs.microsoft.com/es-es/azure/virtual-machines/linux/cli-ps-findimage?toc=%2Fazure%2Fvirtual-machines%2Flinux%2Ftoc.json)
[Tamaño de maquinas virtuales](https://docs.microsoft.com/es-es/azure/virtual-machines/linux/sizes?toc=%2Fazure%2Fvirtual-machines%2Flinux%2Ftoc.json) 

Por último se ha añadido el provisionamiento con un script de Ansible.
~~~

  # Provisionamiento con Ansible
  config.vm.provision :ansible do |ansible|

      ansible.playbook = "provision/playbook.yml"

  end

~~~

Una vez hecho todo lo anterior podemos levantar la máquina `vagrant up --provider=azure`.

![Vagrant Up](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-6.png)

Tras este proceso vamos al nuestro portal azure y podemos ver todos los recursos que se han creado automáticamente.

![Portal Azure](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/img/aplicacion-nube-7.PNG)

Información obtenida de:  

* [Scottlowe](https://blog.scottlowe.org/2017/12/11/using-vagrant-with-azure/)
* [Azure Microsoft](https://azure.microsoft.com/es-es/resources/videos/azure-virtual-machine-creation-and-set-up-using-vagrant-with-corey-fowler/)
* [Returngis](https://www.returngis.net/2015/11/usa-vagrant-con-microsoft-azure/)
* [Ruby Doc](https://www.rubydoc.info/gems/vagrant-azure/1.3.0)
* [Linkedin](https://www.linkedin.com/pulse/azure-devops-vagrant-joão-pedro-soares)
* [Vagrant Azure](https://github.com/Azure/vagrant-azure)
* [Alberto Romeu](https://albertoromeu.com/vagrant-desde-cero/)
* [Adicto al Trabajo](https://www.adictosaltrabajo.com/2014/02/12/vagrant-install/)


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

- **IP pública:** 40.78.6.136
- **DNS:**  porradeportiva.westus.cloudapp.azure.com 

Para ver las rutas activas se puede ver la api que ofrece: [porradepapp.py](https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-/blob/master/src/porradepapp.py).