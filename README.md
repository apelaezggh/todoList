# **Requirements**

Python 2.7.15

# **Install**

## Install requirements.txt

pip install -r requirements.txt

# **Connect to data base**

## 1. Create user '*user*' with password '*password*' and db '*data_base*'

$ sudo su - postgres  
$ psql  
postgres=# CREATE USER *user_selected* WITH PASSWORD '*password*';  
CREATE ROLE  
postgres=# CREATE DATABASE *data_base* WITH OWNER *user*;  
CREATE DATABASE  

## 2. Edit file setting.<setting></setting>py

~~~DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'data_base',
        'USER': 'user_selected',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
~~~

# **Make migrations**

$ python manage.<manage></manage>py makemigrations  
$ python manage.<manage></manage>py migrate  

# **Create superuser for python admin**

$ python manage.<manage></manage>py createsuperuser
Nombre>
Email>
Pass>

# **Run aplication**

$python manage.<manage></manage>py runserver

# **Run python admin**

http://127.0.0.1:8000/admin/

# **Run Rest API test**

http://127.0.0.1:8000/activity/activity

