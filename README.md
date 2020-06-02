# Django_PostgreSQL
# Django is the web framework of python.
This guide will assist in creating web application with Django and PostgreSQL with login, register and fetching data from database.
Following are the steps to be performed for the configuration:
1. Make sure django and postgreSQL is installed.
2. First you need to install Postgres client i.e. “psycopg2”
      ### pip install psycopg2
3. Django uses SQLite in its backend by default. So update database in settings.py(refer myproject/settings.py).
4. Django uses ORM (Object Relational Mapping) Layer. By default Django create database schema once the configuration is done. You just      need to migrate and run.
      ### python manage.py migrate
      ### python manage.py runserver
