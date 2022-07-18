from django.db import models


class User(models.Model):
    # id = autogen?
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    # os_type = enum?
    # packages = list?
    install_docker = models.BooleanField(default=False)
    # docker_images = list?
