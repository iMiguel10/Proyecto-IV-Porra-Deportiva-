# Fabfile to:
#    - Borrar el microservicio
#    - Actualizar el microservicio
#    - Iniciar el microservicio

# Import Fabric's API module
from fabric.api import *

def Borrar():

    # Borramos antiguo codigo
    run('rm -rf Proyecto-IV-Porra-Deportiva-')


def Actualizar():

    # Borramos antiguo codigo
    Borrar

    # Descargamos nuevo repositorio
    run('git clone https://github.com/iMiguel10/Proyecto-IV-Porra-Deportiva-.git')  

    # Instalamos requirements
    run('pip3 install -r Proyecto-IV-Porra-Deportiva-/requirements.txt')


def Iniciar():

     # Iniciamos el servicio web
     run('cd Proyecto-IV-Porra-Deportiva-/src/ && sudo gunicorn porradepapp:app -b 0.0.0.0:80')