# eduNext Coding Challenge

Este es el repositorio de mi challenge. Para gestionar el ambiente de desarrollo, utilicé Anaconda (el cual recomiendo, debido a que es muchísimo más simple que virtualenv). En el archivo [TODO.md](https://github.com/yeguacelestial/edunext-challenge/blob/master/TODO.md) se puede consultar una lista de tareas que se realizaron durante el proceso de esta API.

## Instalar y configurar ambiente de desarrollo con Anaconda

Para configurar el ambiente de desarrollo y sus dependeicas con Anaconda, basta con hacer los siguientes comandos desde la terminal con Anaconda instalada
```
conda env create -f environment.yml
```
Esto re-creará de forma inmediata el ambiente de desarrollo.

## Instalar y configurar ambiente de desarrollo desde otro gestor
Para configurar el ambiente de desarrollo manualmente, se configura dentro del ambiente deseado la versión de ```Python 3.7.7```, y se instalan las dependencias con el siguiente comando
```
pip install -r requirements.txt
```
Esto será suficiente para poder instalar las dependencias requeridas por el proyecto.

## Inicializar API Server
El proyecto de Django se encuentra dentro del directorio:
```002_fun_coding_time/edunext_challenge_django_project```

Ahí se podrá encontrar el archivo ```manage.py``` para inicializar el API Server de este proyecto.

La API estará lista para usarse y recibir peticiones POST desde la siguiente URL:

[http://localhost:8000/payments/paypal/](http://localhost:8000/payments/paypal/)

Se pueden intentar hacer las peticiones necesarias para ver el funcionamiento de este proyecto.

De antemano, quiero agradecerles por cambiar la dinámica de reclutamiento. Más allá de si seré elegido o no para cubrir el puesto de desarrollador back-end, la verdad es que disfruté mucho realizar este reto técnico.