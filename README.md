# Personal-Gallery

# Description  
This is a Django application for personal gallery that allows a user to upload images for other to see and be able to to share by coping the image link.

#### Technologies used
    - Python 3.9
    - HTML
    - Bootstrap 5
    - Heroku
    - Postgresql
    - Django, Django Rest Framework


## Getting Started

These instructions are instruction on getting my application.

### Prerequisites

The following things are needed so as install the application and how to install them

```
Python-3.9.13
pip 3
```

### Installing
Here is
-A step by step series of instructions that tell you how to get a development of the application running

you need to get the necessary requirements

```
$ pip install -r requirements.txt
```

Have a virtual environment

```
$ python3.9 -m venv --without-pip virtual

####  Create the Database
    - psql
    - CREATE DATABASE gallery;
####  .env file
Create .env file and paste paste the following filling where appropriate:

    SECRET_KEY = '<Secret_key>'
    DBNAME = 'tribune'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
    
#### Run initial Migration
    python3.9 manage.py makemigrations gallery
    python3.9 manage.py migrate
    
#### Run the app
    python3.9 manage.py runserver
    Open terminal on localhost:8000

