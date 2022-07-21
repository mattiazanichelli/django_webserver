import json
import os
import requests
from asgiref.sync import sync_to_async

from ..models import OsType


def extract_packages(body):
    split = body.decode("UTF-8").split("&")
    packages = []

    for s in split:
        tmp = s.split("=")
        key = tmp[0]
        value = tmp[1]

        if value == "on" and not (key == "install_docker"):
            packages.append(key)

    return packages


def extract_docker_images(body):
    split = body.decode("UTF-8").split("&")

    user_docker_images = []
    for s in split:
        tmp = s.split("=")
        key = tmp[0]
        value = tmp[1]

        if key == "dockerImage":
            user_docker_images.append(value)

    return user_docker_images


def serialize_user(body):
    fields = body.dict()
    user = {
        'first_name': fields['first_name'],
        'last_name': fields['last_name'],
        'email': fields['email'],
        'os_type': OsType(int(fields['os_type'])).name.lower(),
        'install_docker': fields['install_docker']
    }
    return user


def write_json(user):
    user_json = json.dumps(user)
    file_name = user['last_name'] + '_' + user['first_name'] + ".json"
    with open("./customizo/resources/" + file_name, "w") as outfile:
        outfile.write(user_json)


def generate_iso():
    os.system(os.curdir + '/customizo/resources/./execute.sh')


def read_docker_images():
    docker_images = list()
    with open("./customizo/resources/docker_images", "r") as infile:
        content = infile.read()
    docker_images = content.split("\n")
    return docker_images


def get_docker_images():
    page = 1
    docker_images = list()
    while True:
        url = "https://hub.docker.com/v2/repositories/library/?page=" + str(page)
        response = requests.get(url)

        if response.status_code == 404:
            break

        json_response = response.json()

        for image in json_response['results']:
            docker_images.append(image['name'])

        page += 1
    return docker_images
