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