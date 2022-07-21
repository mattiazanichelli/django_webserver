import json
import os


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

    docker_images = []
    for s in split:
        tmp = s.split("=")
        key = tmp[0]
        value = tmp[1]

        if key == "dockerImage":
            docker_images.append(value)

    return docker_images


def serialize_user(body):
    fields = body.dict()
    user = {
        'first_name': fields['first_name'],
        'last_name': fields['last_name'],
        'email': fields['email'],
        'os_type': fields['os_type'],
        'install_docker': fields['install_docker']
    }
    return user


def write_json(user):
    user_json = json.dumps(user, indent=4)
    file_name = user['last_name'] + user['first_name'] + ".json"
    with open("./customizo/resources/"+file_name, "w") as outfile:
        outfile.write(user_json)


def generate_iso():
    os.system(os.curdir+'/customizo/resources/./execute.sh')
