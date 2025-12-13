from .base import *
DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'luke10.pythonanywhere.com']
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "luke10$info390mg-mysql-database",
        "USER": "mohitg2",
        "PASSWORD": "graingerlibrary",
        "HOST": "luke10.mysql.pythonanywhere-services.com",
        "PORT": "3306",
    }
}