import mimetypes
import os
from wsgiref.util import FileWrapper

from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse

# from .forms import UserForm
# from .models import User
from .business_logic import services


def index_page(request):
    return render(request, 'index.html')


def form_page(request):
    if request.method == 'POST':
        user = services.serialize_user(request.POST)
        user['packages'] = services.extract_packages(request.body)
        user['docker_images'] = services.extract_docker_images(request.body)
        services.write_json(user)
        services.generate_iso()
        return redirect('download')

    if request.method == 'GET':
        return render(request, 'form.html')


def download_page(request):
    if request.method == 'POST':
        file_name = 'Zanichelli-Mattia-custom-server.iso'
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
