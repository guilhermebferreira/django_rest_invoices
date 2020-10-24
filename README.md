# Invoices REST API

Rest api developed using Django Rest Framework, 
with mysql database and unit tests with mocked methods 
to avoid manipulating on database while running the tests

## Database

To use the database container, run

    cd mysql
    docker-compose up

To use a local database, update the database settings at `api/settings.py`
    
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': '0.0.0.0',
        'PORT': '3306',
    }
}

## Setup
    virtualenv venv
    . venv/bin/active
    pip install -r requirements.txt
    
    ./mange.py migrate

## Test
    ./manage.py test
    
    
## Run
    ./manage.py runserver
    
    
# API Usage

All methods related to invoices require token authentication. So first you need to register a new user

And then use the access token to make requests

## Registration
    [POST] /api/auth/registration/
Body:
    
    {
       'username': 'username',
       'email': 'email@email.com',
       'password1': 'password',
       'password2': 'password_confirmation',
    }
Response:

    {
       'key': Token
    }
    
## Login    
    [POST] /api/auth/login/
Body:
    
    {
       'username': 'username',
       'password': 'senha',
    }
Response:

    {
       'key': Token
    }

##  Authorization

All requests must include the authorization token

    Authorization: Token <<token>>


Or, the request will only return a message `Authentication credentials were not provided.`

## GET | Retrieve

    [GET] /api/invoices

### Filter

Filter params:
   - document
   - reference_year
   - reference_year

    [GET] /api/invoices/?order_by=-document&document=text test eeee&reference_year=2020
    
    
## Ordering

Order params:
   - document
   - reference_year
   - reference_year
   
Default: `ASC`, use `-` to `DESC`

     [GET] /api/invoices/?order_by=document
    
Will result: `ORDER BY document ASC`    
and    
    
     [GET] /api/invoices/?order_by=-document
    
    ORDER BY document DESC
    
## Pagination

Results will be returned on pages of up to 100 items

Use the urls `next` and `previous` to navigate through the pages, 
or the `limit` and `offset` parameters to access a specific page

    http://127.0.0.1:8000/api/invoices/?limit=2&offset=2
    
## Post | Create
    [POST] /api/invoices/
Body:

    {
        'reference_month':10
        'reference_year':2020
        'description':'description'
        'amount':999.99
        'document':'document'
    }
    

## Delete | Deactivation
    [DELETE] /api/invoices/<:id>
Response:

    {
        'reference_month':10
        'reference_year':2020
        'description':'description'
        'amount':999.99
        'document':'document'
        'is_active': False,
        'created_at': 'creation date',
        'deactive_at': 'decativation date'
    }
    
The invoice will not be deleted from the database, but it will be disabled