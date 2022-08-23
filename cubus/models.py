# import uuid
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from typing import Optional
# from pydantic import Field
from enum import Enum


class OsType(Enum):
    INTRUSION_DETECTION = 1
    NETWORK_MONITORING = 2

# class ISO:
#
#     def __init__(self):
#         pass
#
#     # id: str = Field(default_factory=uuid.uuid4, alias="_id")
#     name: str = Field(...)
#     os_type: OsType = Field(...)
#     packages: Optional[list]
#     include_docker_images: bool = Field(...)
#     docker_images: Optional[list]


# class User:
#
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     password: models.CharField(max_length=100)
#     ISOs: Optional[list]

