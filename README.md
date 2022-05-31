# Contacts Management API
Rest API for managing contacts. The application was implemented using Django REST framework and has the following features:
- Rest API;
- Token Authentication;
- Pagination.

## Requirements
 - Python 3.8.5;
 - Django 3.2;
 - PostgreSQL 13.

## Installing
Create a user in the database with database creation permission and with the following credentials:
- Username: horus_user
- Password: horus_password

Create a database named "horus_challenge_db".

If you need to customize database access, update the variable named DATABASES located in horus_challenge/settings.py.

To install the application, run the following commands in the project root folder:
```
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata db.json
```
A user with the following credentials will be created:
- Username: horus
- Password: horus12345678

## Running
To run the application, execute the following commands in the project root folder:
```
python manage.py runserver
```

The api will be available at http://127.0.0.1:8000

## Testing
Make sure that the database user has permission to create databases. To test the application, run the following commands in the project root folder:
```
python manage.py test
```
The test routines are located in the api/tests.py file. The following tests will be performed:
- Add a contact;
- Update the contact name;
- Update the contact phone number;
- Delete a contact;

## Endpoints
The API must be accessed via token authentication. Add the key "Authorization" with the value "Token <token>" to the request's header.
The api has the following endpoints:
### Get a user's token
- Endpoint: /api-auth/token/
- Method: POST
- Example:
```
curl -X POST -F 'username=horus' -F 'password=horus12345678' http://127.0.0.1:8000/api-auth/token/
```
### Get authenticated user's information
- Endpoint: /api-auth/user-info/
- Method: GET
- Example:
```
curl -X GET -H 'Authorization: Token eb55c58b680a96877b31b0156a7f07cc849c91a9' http://127.0.0.1:8000/api-auth/user-info/
```
### List user's contacts
- Endpoint: /api-v1/contacts/
- Method: GET
- Example:
```
curl -X GET -H 'Authorization: Token eb55c58b680a96877b31b0156a7f07cc849c91a9' http://127.0.0.1:8000/api-v1/contacts/
```
### Create a contact:
- Endpoint: /api-v1/contacts/
- Method: POST
- Example:
```
curl -X POST -F 'owner=2' -F 'name=Rafael Albuquerque' -F 'telephone=88999034444' -H 'Authorization: Token eb55c58b680a96877b31b0156a7f07cc849c91a9' http://127.0.0.1:8000/api-v1/contacts/
```
### Update a contact
- Endpoint: /api-v1/contacts/<int:contato_id>/
- Method: PUT
- Example:
```
curl -X PUT -F 'owner=2' -F 'name=Rafael Moreira' -F 'telephone=88999034443' -H 'Authorization: Token eb55c58b680a96877b31b0156a7f07cc849c91a9' http://127.0.0.1:8000/api-v1/contacts/1/
```
### Delete a contact
- Endpoint: /api-v1/contacts/<int:contato_id>/
- Method: DELETE
- Example:
```
curl -X DELETE -H 'Authorization: Token eb55c58b680a96877b31b0156a7f07cc849c91a9' http://127.0.0.1:8000/api-v1/contacts/1/
```
