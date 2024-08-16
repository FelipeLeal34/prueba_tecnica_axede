PASOS PARA INSTALAR EL PROYECTO

1. Clonar el repositorio
2. Instalar xampp 
3. Encender los servicios de apache y mysql
3. Crear una base de datos en phpmyadmin llamada "hoteles"
4. importar el archivo llamado hotelesbackup.sql

5. Ingresar a la carpeta del PROYECTO
6. instalar virtualenv globalmente con pip install virtualenv
7. Crear un entorno virtual con virtualenv llamado "venv" con el comando :  virtualenv venv
8. Desde la raiz del proyecto ejecutar el comando pip install -r requirements.txt

9. ejecutar el comando python manage.py makemigrations y migrate
10. ejecutar el comando python manage.py runserver


//NOTA : Se subió el archivo .env al repositorio por el contexto del ejercicio.