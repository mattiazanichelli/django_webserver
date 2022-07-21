from django.db import models
from enum import Enum
import json


class OsType(Enum):
    INTRUSION_DETECTION = 1
    NETWORK_MONITORING = 2


# class User:
#
#     first_name: str
#     last_name: str
#     email: str
#     os_type: OsType
#     packagkes: list
#     install_docker: bool
#     docker_images: list
#
#     def __str__(self):
#         return self.first_name + " " + self.last_name


# class OsType(models.TextChoices):
#     INTRUSION_DETECTION = 'ID', 'Intrusion Detection'
#     NETWORK_MONITORING = 'NM', 'Network Monitoring'
#
#
# class User(models.Model):
#     # id = models.IntegerField(primary_key=True)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.CharField(max_length=100)
#     os_type = models.IntegerField(default=0)
#     packages = models.CharField(max_length=200, blank=True)
#     install_docker = models.BooleanField(default=False)
#     docker_images = models.CharField(max_length=200, blank=True)
#
#     def set_packages(self, packages_list):
#         self.packages = json.dumps(packages_list)
#
#     def get_packages(self):
#         return json.loads(self.packages)
#
#     def set_docker_images(self, images):
#         self.docker_images = json.dumps(images)
#
#     def get_docker_images(self):
#         return json.loads(self.docker_images)

