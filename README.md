# GST TAX MANAGEMENT API SYSTEM

# Main points for creating a REST API in Django REST framework.

 find out steps to creating a REST API.

    Set-Up Virtual Environment.
    Set-Up Django
    Create a model for the database that the Django ORM will manage.
    Set-Up Django Rest Framework
    Serialize the model data from step-3
    Create the URI endpoint to view the serialized data.

# 1. Set-Up Virtual Environment

sudo apt update

sudo apt install python3-django

sudo apt install python3-pip

sudo apt install python3-venv

mkdir APIWebsite

cd APIWebsite

python3.6 -m venv wenv

source wenv/bin/activate

# 2. Set-Up Django

pip install django

django-admin startproject Website

# Check Django Server is working properly or not

python manage.py runserver

# Creating the app

python manage.py startapp api

# Migrate the database

python manage.py makemigrations

python manage.py migrate

# Create Super User

python manage.py createsuperuser

python manage.py runserver

# 3.Set-Up the Django Rest Framework

pip install djangorestframework

python manage.py runserver

# Root Path

User Registration for GST TAX: http://127.0.0.1:8000/api/register/

User Login for GST TAX(If you already registered): http://127.0.0.1:8000/api/login/

Registerd User Logout: http://127.0.0.1:8000/api/logout/

Admin Login for GST TAX(If you already create superuser): http://127.0.0.1:8000/api/user/
Note: Use Superuser credentials

Show User Invoice of User for GST TAX: http://127.0.0.1:8000/api/list/

Update Profile for Current User with the help of id: http://127.0.0.1:8000/api/updateprofile/id/

Delete Specific User Profile: http://127.0.0.1:8000/api/delete/id

Show SuperUser Invoice to get info about all admins who manage user invoices: http://127.0.0.1:8000/api/detail/

