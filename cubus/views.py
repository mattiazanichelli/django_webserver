import mimetypes
import os
from wsgiref.util import FileWrapper

from django.http import StreamingHttpResponse
from django.shortcuts import render, redirect
from pymongo import MongoClient

from webserver.settings import MONGO_HOST, MONGO_PORT, MONGO_USERNAME, MONGO_PASS
from .business_logic import services

# TODO: Find a way to get images online asynchronously
# Call async function to get docker images
# thread = threading.Thread(target=services.get_docker_images(), daemon=True)
# thread.start()
# thread.join()
docker_images = services.read_docker_images()

# Create and activate Mongo database
client = MongoClient(host=MONGO_HOST, port=int(MONGO_PORT), username=MONGO_USERNAME, password=MONGO_PASS)
customizo = client['cubus']
users = customizo['users']
current_user = ""


# Views
def index_page(request):
    global current_user
    current_user = ""
    return render(request, 'index.html')


def form_page(request):
    global docker_images
    context = {"docker_images": docker_images}

    if request.method == 'POST':
        user = services.serialize_user(request.POST)
        user['packages'] = services.extract_packages(request.body)
        user['docker_images'] = services.extract_docker_images(request.body)

        services.write_json(user)
        users.insert_one(user)
        services.generate_iso()

        global current_user
        current_user = user['last_name'] + '-' + user['first_name']
        return redirect('download')

    if request.method == 'GET':
        return render(request, 'form.html', context=context)


def download_page(request):
    if request.method == 'POST':
        file_name = current_user + '-custom-server.iso'
        # file_name = current_user + '.json'
        file_path = os.curdir + '/cubus/resources/' + file_name
        chunk_size = 8192
        mime_type = mimetypes.guess_type(file_path)[0]
        response = StreamingHttpResponse(FileWrapper(open(file_path, 'rb'), chunk_size), content_type=mime_type)
        response['Content-Length'] = os.path.getsize(file_path)
        response['Content-Disposition'] = "attachment; filename=%s" % file_name
        return response
    if request.method == 'GET':
        if current_user == "":
            return render(request, 'index.html')
        else:
            return render(request, 'download.html')


def guide_page(request):
    return render(request, 'guide.html')
