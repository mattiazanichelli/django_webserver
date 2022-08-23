import json
import os
import crypt

import django.http
import requests

from ..models import OsType


def extract_packages(body):
    split = body.decode("UTF-8").split("&")
    packages = []

    for s in split:
        tmp = s.split("=")
        key = tmp[0]
        value = tmp[1]

        if value == "on" and not (key == "include_docker_images"):
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


def serialize_iso(post):
    if isinstance(post, django.http.QueryDict):
        fields = post.dict()
    else:
        fields = post
    iso = {
        'name': fields['isoName'],
        'os_type': OsType(int(fields['os_type'])).name.lower(),
        'include_docker_images': fields['include_docker_images']
    }
    return iso


def serialize_user(post):
    if isinstance(post, django.http.QueryDict):
        fields = post.dict()
    else:
        fields = post
    user = {
        'first_name': fields['first_name'],
        'last_name': fields['last_name'],
        'email': fields['email'],
        'password': crypt.crypt(fields['password'], 'salt'),
        'creations': [],
    }
    return user


def write_json(iso):
    iso_json = json.dumps(iso)
    file_name = iso['name'] + ".json"
    with open("./cubus/resources/" + file_name, "w") as outfile:
        outfile.write(iso_json)


def generate_iso():
    os.system(os.curdir + '/cubus/resources/./execute.sh')


def read_docker_images():
    docker_images = list()
    with open("./cubus/resources/docker_images", "r") as infile:
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
