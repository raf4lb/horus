# Aplicação Backend do Desafio Horus
API Rest para que um usuário possa gerenciar uma lista de contatos. A aplicação foi implementada usando Django REST framework e possui os seguintes recursos:
- API Rest;
- Autenticação via token;
- Paginação.

## Requerimentos
 - Python 3.8.5;
 - Django 3.2;
 - PostgreSQL 13.

## Instalação
Criar o usuário no banco de dados com permissão para criar banco de dados e as seguintes credenciais:
- Usuário: horus_user
- Senha: horus_password
 
Caso seja necessário personalizar o acesso ao banco de dados, basta configurar os campos do dicionário DATABASES localizado em horus_challenge/settings.py.

Para instalar a aplicação, basta executar os seguintes comandos na pasta do projeto:
```
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata db.json
```
Será criado um usuário com as seguintes credenciais:
- Usuário: horus
- Senha: horus12345678

## Rodando
Para rodar a aplicação, basta e executar o seguinte comando na pasta do projeto:
```
python manage.py runserver
```

A api estará acessível no endereço http://127.0.0.1:8000

## Testando
Certifique-se de que o usuário horus_user tenha permissão para criar bancos de dados. Para testar a aplicação,  basta e executar o seguinte comando na pasta do projeto:
```
python manage.py test
```
As rotinas de teste estão localizadas no arquivo api/tests.py. Os seguintes testes serão realizados:
- Adicionar um contato;
- Editar o nome de um contato;
- Editar o telefone de um contato;
- Excluir um contato;

## Endpoints
Consumo com autenticação via token. Adicionar ao header a chave "Authorization" com o valor "Token <token>".
A api possui os seguntes endpoints:
### Acessar token de um usuário
- Endpoint: /api-auth/token/
- Método: POST
- Exemplo:
```
curl -X POST -F 'username=horus' -F 'password=horus12345678' http://127.0.0.1:8000/api-auth/token/
```
### Acessar informações do usuário autenticado
- Endpoint: /api-auth/user-info/
- Método: GET
- Exemplo:
```
curl -X GET -H 'Authorization: Token eb55c58b680a96877b31b0156a7f07cc849c91a9' http://127.0.0.1:8000/api-auth/user-info/
```
### Listagem de contatos de um usuário
- Endpoint: /api-v1/contacts/
- Método: GET
- Exemplo:
```
curl -X GET -H 'Authorization: Token eb55c58b680a96877b31b0156a7f07cc849c91a9' http://127.0.0.1:8000/api-v1/contacts/
```
### Criação de um contato:
- Endpoint: /api-v1/contacts/
- Método: POST
- Exemplo:
```
curl -X POST -F 'owner=2' -F 'name=Rafael Albuquerque' -F 'telephone=88999034444' -H 'Authorization: Token eb55c58b680a96877b31b0156a7f07cc849c91a9' http://127.0.0.1:8000/api-v1/contacts/
```
### Atualização de contato
- Endpoint: /api-v1/contacts/<int:contato_id>/
- Método: PUT
- Exemplo:
```
curl -X PUT -F 'owner=2' -F 'name=Rafael Moreira' -F 'telephone=88999034443' -H 'Authorization: Token eb55c58b680a96877b31b0156a7f07cc849c91a9' http://127.0.0.1:8000/api-v1/contacts/1/
```
### Exclusão de contato
- Endpoint: /api-v1/contacts/<int:contato_id>/
- Método: DELETE
- Exemplo:
```
curl -X DELETE -H 'Authorization: Token eb55c58b680a96877b31b0156a7f07cc849c91a9' http://127.0.0.1:8000/api-v1/contacts/1/
```