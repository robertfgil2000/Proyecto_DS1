<p align='center'>
  <img width='200' heigth='225' src='https://user-images.githubusercontent.com/62605744/171186764-43f7aae0-81a9-4b6e-b4ce-af963564eafb.png'>
</p>

# Proyecto Desarrollo de Software I
- Proyecto de la asignatura Desarrolo de Software I
- Semestre 2023-I
- Profesor: Carlos Mauricio Gaona Cuevas

## Autores
- Robert Fernando Gil Trujillo - 2022985
- Diana Carolina Micolta Céspedes - ?????????
- Marcelo Alejandro García Millán - 201941427
- Janiert Sebastián Salas Castillo - ?????????
- Diego Fernando Victoria López - ?????????


## Como ejecutar el código con ambiente virtual:


pip install virtualenv 


<br>
Para crear el ambiente virtual llamado"venv":


python -m venv venv


<br>
Para ejecutar el ambiente virtual (sólo en Windows):


.\venv\Scripts\activate


<br>
Realizar las instalaciones de las dependencias (procure haber ejecutado el ambiente virtual):


pip install -r requirements.txt

<br>
Para realizar las migraciones a la base de datos de postgres (NOTA: Asegurarse de las respectivas credenciales de acceso a su BD local):


python manage.py makemigrations
python manage.py migrate

<br>
Para ejecutar el servidor Django:


python manage.py runserver


<br>
Para cerrar el ambiente virtual:


deactivate
