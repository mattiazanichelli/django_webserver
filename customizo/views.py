import mimetypes
import os
from wsgiref.util import FileWrapper

from django.http import StreamingHttpResponse
from django.shortcuts import render, redirect
from pymongo import MongoClient

from webserver.settings import MONGO_HOST, MONGO_PORT, MONGO_USERNAME, MONGO_PASS
from .business_logic import services
# from .models import User

client = MongoClient(host=MONGO_HOST, port=int(MONGO_PORT), username=MONGO_USERNAME, password=MONGO_PASS)
customizo = client['customizo']
users = customizo['users']
current_user = ""


def index_page(request):
    return render(request, 'index.html')


def form_page(request):
    if request.method == 'POST':
        user = services.serialize_user(request.POST)
        user['packages'] = services.extract_packages(request.body)
        user['docker_images'] = services.extract_docker_images(request.body)
        services.write_json(user)
        users.insert_one(user)
        # services.generate_iso()
        global current_user
        current_user = user['last_name'] + '_' + user['first_name']
        return redirect('download')

    if request.method == 'GET':
        return render(request, 'form.html')


def download_page(request):
    if request.method == 'POST':
        # file_name = current_user + '-custom-server.iso'
        file_name = current_user + '.json'
        file_path = os.curdir + '/customizo/resources/' + file_name
        # file = os.path.basename(file_path)
        chunk_size = 8192
        mime_type = mimetypes.guess_type(file_path)[0]
        response = StreamingHttpResponse(FileWrapper(open(file_path, 'rb'), chunk_size), content_type=mime_type)
        response['Content-Length'] = os.path.getsize(file_path)
        response['Content-Disposition'] = "attachment; filename=%s" % file_name
        return response
    if request.method == 'GET':
        return render(request, 'downloadPage.html')


def help_page(request):
    return render(request, 'help.html')
