# jwt_authentication

Aplicação de autenticação e criação básica de usuário utilizando o jwt.

## Configuração Inicial:

É necessário configurar as variáveis do arquivo .env

| Variável   | Configuração                                                      |
| ---------- | ----------------------------------------------------------------- |
| DB_URI     | Configurar a conexão com o seu banco de dados                     |
| SECRET_KEY | Chave para codificação e decodificação dos passwords dos usuários |

## Rotas:

## Created User:

`POST /users/signup`

REQUEST FORMAT

```json
{
  "name": "John",
  "last_name": "Wick",
  "email": "johnwick@gmail.com",
  "password": "BabaYaga"
}
```

---

RESPONSE FORMAT STATUS 201

```json
{
  "id": "32391562-fd8a-4805-932b-64f1aa871273",
  "name": "John",
  "last_name": "Due",
  "email": "johnwick@gmail.com"
}
```

---

## Login User:

`POST /users/signin`

REQUEST FORMAT

```json
{
  "email": "johnwick@gmail.com",
  "password": "BabaYaga"
}
```

RESPONSE FORMAT STATUS 200

```json
{
  "acess_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0NzM2NTcxNiwianRpIjoiYjRhOTdlOWEtNjVmNS00ZGM3LTg4OTAtOTY5ZmY2MjE1YzA4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6IjMyMzkxNTYyLWZkOGEtNDgwNS05MzJiLTY0ZjFhYTg3MTI3MyIsIm5hbWUiOiJHZXJhbGRvIiwibGFzdF9uYW1lIjoiU2FybWVudG8iLCJlbWFpbCI6ImdlcmFzYXJtZW50b0BvdXRsb29rLmNvbSJ9LCJuYmYiOjE2NDczNjU3MTYsImV4cCI6MTY0NzM2NjYxNn0.5ArwUpmOjcw4nOoqw4M61tkhbQtKN8Onvon3-jgL82M"
}
```

---

## Get specific User:

`GET /users/profile`

REQUEST FORMAT

> header {

    Authorization: Bearer token

}

Bearer token é o acess token gerado ao realizar o login

RESPONSE FORMAT STATUS 200

```json
{
  "id": "32391562-fd8a-4805-932b-64f1aa871273",
  "name": "John",
  "last_name": "Due",
  "email": "johnwick@gmail.com"
}
```

---

## Get all Users:

`GET /users`

RESPONSE FORMAT STATUS 200

```json
{
  "users": [
    {
      "id": "e931d4d6-5bce-4cda-b280-f66d3facc480",
      "name": "John",
      "last_name": "Wick",
      "email": "johnwick@gmail.com"
    }
  ],
  "page": 1,
  "total_pages": 1
}
```

---

## Patch specific User:

`PATCH /users/profile`

REQUEST FORMAT

> header {

    Authorization: Bearer token

}

Bearer token é o acess token gerado ao realizar o login

RESPONSE FORMAT STATUS 200

```json
{
  "id": "32391562-fd8a-4805-932b-64f1aa871273",
  "name": "John",
  "last_name": "Due",
  "email": "johnwick@gmail.com"
}
```

---

## Delete specific User:

`Delete /users/profile`

REQUEST FORMAT

> header {

    Authorization: Bearer token

}

Bearer token é o acess token gerado ao realizar o login

RESPONSE FORMAT STATUS 200

```json
{ "msg": "User John Wick has been deleted" }
```
