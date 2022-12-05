# Django multi-tenant local setup

### About

A sample django application which demonstrates multi-tenant feature

### Application multi-tenancy model
Semi-isolated - Each tenant will share the same database but each will have their own schema.

### Tech Stack

Following is the tech stack being used for main project:

* [Django 3.2] - The core Web Framework
* [django-tenant 3.4.7] - To enable multi tenant feature
* [Python 3.9] - As the programming language
* [PostgreSQL 10] - As the main datastore

### Project Setup

* Create Virtual env
```
python -m venv <env-name>
```

* Activate virtual env
```
source <env-name>/bin/activate
```

* Install Requirements
```
pip install -r requirements.txt
```

* Make sure project is running
```
python manage.py runserver
```

##### Setting up Django Tenants
* Setup Middleware and Database. First create a PostgreSQL database and note the user and password
* Add django_tenants middleware
```
# add this at the top
'django_tenants.middleware.main.TenantMainMiddleware',
```
* Setup DB connection
```
DATABASES = {
    'default': {
        # Tenant Engine
        'ENGINE': 'django_tenants.postgresql_backend',
        # set database name
        'NAME': '<your-db-name>',
        # set your user details
        'USER': '<user>',
        'PASSWORD': '<password>',
        'HOST': '<host>',
        'POST': '<port>'
    }
}

# DATABASE ROUTER
DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)
```

* Django App for tenants - customers
```
# created by running following command
python manage.py startapp customers
```

* Configured tenant model and domain by adding following code to settings.py file
```
TENANT_MODEL = "customers.Client"
TENANT_DOMAIN_MODEL = "customers.Domain"
```

* Sample tenant specific app
```
# created by running following command
python manage.py startapp article
```
* Setup Shared and Tenants Apps
```
# Application definition
"""
    These app's data are stored on the public schema
"""
SHARED_APPS = [
    'django_tenants',  # mandatory
    'customers',  # you must list the app where your tenant model resides in

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'article',
]
"""
    These app's data are stored on their specific schemas
"""
TENANT_APPS = [
    # The following Django contrib apps must be in TENANT_APPS
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',

    # tenant-specific apps
    'article',
]

INSTALLED_APPS = list(SHARED_APPS) + [
    app for app in TENANT_APPS if app not in SHARED_APPS
]
```

* Create required models under customers and article app and make migrations and apply to DB
```
# create migrations files
python manage.py makemigrations
# Apply migrations
python manage.py migrate_schemas
```

* Setup Initial User, Tenant and Admin
```
# create first user
python manage.py createsuperuser
# Create the Public Schema
python manage.py create_tenant
# Create the Administrator
python manage.py create_tenant_superuser
```

* Test by running
```
python manage.py runserver
```



