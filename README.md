# About
This repository is a basic template of Django project with PostgreSQL data base  
and NGINX web server using Docker Compose. If you new or completly unfamiliar with  
Docker and Docker Compose this repo can help you to deploy your Django project fast.  

Docker Compose will create 3 containers in following order:  
1. **postgres** - contaner where data base is running. Adds **/data/db** directory where  
postgres files are stored.

2. **django** - contaner where your app is stored. It also create database for your app  
(see **create_db.py**) and make & apply migrations.

3. **nginx** - container with NGINX web-server. Config file stored in /nginx/ directory.  

## Prerequirements
Install Docker version **3.2.1** or above: https://docs.docker.com/engine/install/  
>**Note:** If you want to use erlier version of Docker also install Docker Compose.

# HOWTO
1. Clone this repository into machine you want to deploy.
2. Run some commands:  
```
docker compose build 
```
```
docker compose up -d
```
3. That's it! Go to  http://127.0.0.1 and see Django successfully installation message.

# FAQ

### Static files
Afrer installation Django collect all your static files in `/staticfiles` dir, wich  
is added in to `.gitignore`.

### Using Django dev server
If you want to switch to Django development server just change database ip address  
in **settings.py** to localhost (or any other server where your pgsql is running):
```
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.postgresql',  
        'NAME': 'django_db',  
        'USER': 'django',  
        'PASSWORD': 'django',  
        # 'HOST': '172.18.0.1',   # comment to run locally  
        'HOST': '127.0.0.1',  # uncomment to run locally  
        'PORT': '5432',  
    }  
}  
```

### Connecting to container's shell
In order to connect to Django container's shell to execute some commands,  
(like django-admin and etc.) run following command:
```
docker exec -it django /bin/bash
```
If you want to connect to other container just change container name in  command above  
to other services's name defined in **docker-compose.yml**

### Adding Django fixtures
Docker Compose file is prepared for uploading your initial data. It uses  **initial_data.json**  
file for that. You can generate it onse you filled database with needed data. In order to do  
that run following command: 
```
django-admin dumpdata --exclude=auth --exclude=contenttypes -o initial_data.json
```
Learn more in [docs](https://docs.djangoproject.com/en/4.1/ref/django-admin/#dumpdata).
