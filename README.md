# Invoices REST API

## Setup
    virtualenv venv
    . venv/bin/active
    pip install -r requirements.txt

## Test
    ./manage.py test
    
    
## Run
    ./manage.py runserver
    
    
# API

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

    http://127.0.0.1:8000/api/invoices/?order_by=document
    
Will result: `ORDER BY document ASC`    
and    
    
    http://127.0.0.1:8000/api/invoices/?order_by=-document
    
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