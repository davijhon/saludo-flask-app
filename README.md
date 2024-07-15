
## Instalacion
Añadir un archivo `.env` con las siguientes variables, para la base de datos.

```
saludo-flask-app/
    ├── Dockerfile
    ├── app.py
    ├── docker-compose.yaml
    ├── requirements.txt
    └── .env <----------- (AQUI)
```
Dentro de el,las variables: 
```
# DATABASE
POSTGRES_DB=greetings_db
DB_ENGINE="django.db.backends.postgresql"
POSTGRES_USER=postgres
POSTGRES_PASSWORD="" <---- (TU PASSWORD AQUI)
DB_HOST=db
DB_PORT=5432
```


Correr los siguientes comandos

```
> $ docker compose build
> $ docker compose up
```

## TEST

Creando Saludos 
![image](https://github.com/user-attachments/assets/3888db67-e3f7-4f9d-9fb4-b8386be5f57b)


Obteniendo lista de saludos
![image](https://github.com/user-attachments/assets/d8f07ec8-7042-4758-8551-e8339ae567a6)

Obteniendo un saludo en especifico
![image](https://github.com/user-attachments/assets/0bd9a74d-0d54-4f13-8bf1-da7273021b7e)
