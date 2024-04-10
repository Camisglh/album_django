## A album site for openly displaying your projects

----
### Stack:
<div align="center">
    <img src="https://skillicons.dev/icons?i=python,django,postgresql,redis,rabbitmq,docker" /><br>
</div>

### How run

Clone repository
```bash
    git clone https://github.com/Camisglh/album_django.git
    cd album_django
    touch .env
```

Create file .env
```env
# DJANGO
SECRET_KEY = ''
#'django-insecure-vrry$7m4@=&*rp^ro1i6i_2)afr!8t!8c29vnx-5#7bhws-yen'
NAME = ''
 #'album'
USER = ''
PASSWORD = ''
HOST = ''
PORT = ''

# REDIS
REDIS_HOST=
 #127.0.0.1
REDIS_PORT=
#6379
REDIS_DB=
#0

# CELERY
CELERY_BROKER_URL=
 #amqp://guest:guest@localhost:5672/
CELERY_RESULT_BACKEND=
#django-db
CELERY_ACCEPT_CONTENT=
 #application/json
CELERY_TASK_SERIALIZER=
CELERY_RESULT_SERIALIZER= 
CELERY_TIMEZONE= 
CELERY_BEAT_SCHEDULER=
 #django_celery_beat.schedulers:DatabaseScheduler

```
#### Home
```bash
    # Make sure you are running postgresql, redis and rabbitmq
    python -m venv venv
    pip install -i requirements.txt
    celery -A src worker -l info
    python manage.py runserver
```
#### Docker
```bash
    docker build -t album .
    docker run -p 8000:8000 album
```

-----

Screenshots

Main page
![img.png](media_readme%2Fimg.png)

Profile
![profle.png](media_readme%2Fprofle.png)

Add photo
![add_photo.png](media_readme%2Fadd_photo.png)

Register
![register.png](media_readme%2Fregister.png)

Login
![login.png](media_readme%2Flogin.png)
