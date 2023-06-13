# Django_User_Authentication_Example

This code demonstrates a simple Django website with user authentication and registration form. 


# Running intructions

## Create a virtual environment

Create virtual environment in a console:

`python -m venv myenv`

or by adding Python interpreter in your editor's settings. 

## Activate the virtual environment

### On Windows

'myenv\Scripts\activate'

### On macOS/Linux

'source myenv/bin/activate'

## Install requirements

'pip install -r requirements.txt'

## Configure settings file

Create a local settings file: In the project's settings directory, create a file named local_settings.py to store local development settings. This file will override certain settings when running the project locally:
'# settings/local_settings.py
from .settings import *

# Override settings as needed for local development
DEBUG = True
# ...
'
or alternatively run in a console:

'django-admin startproject app' 

and copy and paste your newly generated sekret key to your settings file:

"SECRET_KEY = 'your_secret_key_here'"

## Run migrations

Apply the database migrations to set up the project's database schema:

'python manage.py migrate'

## Create a superuser (optional)

'python manage.py createsuperuser'

## Run the development server

'python manage.py runserver'

The development server should start, and you can access the application by visiting http://localhost:8000 or http://127.0.0.1:8000 in your web browser.




