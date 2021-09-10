#Install

Install requirements.txt

~$ python install -r requirements.txt

#Create user and data base

Create user 'apg' with password '12345' and db 'db_todolist'

~$ sudo su - postgres
~$ psql
postgres=# CREATE USER user WITH PASSWORD '12345';
CREATE ROLE
postgres=# CREATE DATABASE db_todolist WITH OWNER user;
CREATE DATABASE

#Make migrations

~$ python manage.py makemigrations
~$ python manage.py migrate

#Create superuser for python admin

~$ python manage.py createsuperuser
Nombre>
Email>
Pass>

#Run python admin

http://127.0.0.1:8000/admin/

#Run rest API test

http://127.0.0.1:8000/activity/activity

