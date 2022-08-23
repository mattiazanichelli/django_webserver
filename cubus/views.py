import mimetypes
import os
import crypt
from wsgiref.util import FileWrapper

from django.contrib import messages
from django.http import StreamingHttpResponse
from django.shortcuts import render, redirect
from pymongo import MongoClient

from webserver.settings import MONGO_HOST, MONGO_PORT, MONGO_USERNAME, MONGO_PASS
from .business_logic import services

docker_images = services.read_docker_images()

# Create and activate Mongo database
client = MongoClient(
    host=MONGO_HOST,
    port=int(MONGO_PORT),
    username=MONGO_USERNAME,
    password=MONGO_PASS,
)
cubus = client['cubus']
users = cubus['users']


# Views
def index_page(request):
    return render(request, 'index.html')


def create_page(request):
    if 'authenticated' not in request.session.keys():
        request.session['next'] = 'create'
        return redirect('login')

    global docker_images
    context = {"docker_images": docker_images}

    if request.method == 'POST':
        iso = services.serialize_iso(request.POST)
        iso['packages'] = services.extract_packages(request.body)
        iso['docker_images'] = services.extract_docker_images(request.body)

        services.write_json(iso)
        user = request.session['user']
        user['creations'] += [iso]
        user_filter = {
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'email': user['email']
        }
        new_value = {"$set": {'creations': user['creations']}}
        users.update_one(user_filter, new_value)
        request.session['user'] = user

        services.generate_iso()

        return redirect('download')

    if request.method == 'GET':
        return render(request, 'create.html', context=context)


def download_page(request):
    if 'authenticated' not in request.session.keys():
        return redirect('index')

    if request.method == 'POST':
        user = request.session['user']
        file_name = user['creations'][-1]['name'] + ".iso"
        file_path = os.curdir + '/cubus/resources/' + file_name
        chunk_size = 8192
        mime_type = mimetypes.guess_type(file_path)[0]
        response = StreamingHttpResponse(FileWrapper(open(file_path, 'rb'), chunk_size), content_type=mime_type)
        response['Content-Length'] = os.path.getsize(file_path)
        response['Content-Disposition'] = "attachment; filename=%s" % file_name
        return response
    if request.method == 'GET':
        return render(request, 'download.html')


def guide_page(request):
    return render(request, 'guide.html')


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = crypt.crypt(request.POST.get('password'), 'salt')
        user = users.find_one({"email": email, "password": password})
        if user is None:
            messages.error(request, 'This user does not exists!')
            return render(request, 'login.html')
        else:
            request.session['authenticated'] = True
            current_user = user
            current_user['_id'] = str(user['_id'])
            request.session['user'] = current_user
            request.session.set_expiry(0)  # When the user close the browser

            if request.session['next'] == 'profile':
                return redirect('profile')
            elif request.session['next'] == 'create':
                return redirect('create')
            else:
                return redirect('index')

    if request.method == 'GET':
        return render(request, 'login.html')


def register_page(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        user = services.serialize_user(request.POST)
        if users.find_one({
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'email': user['email']
        }) is None:
            users.insert_one(user)
        return redirect('profile')


def profile_page(request):
    if request.method == 'POST':
        request.session.flush()
        return redirect('index')
    if request.method == 'GET':
        if 'authenticated' not in request.session.keys():
            request.session['next'] = 'profile'
            return redirect('login')
        is_authenticated = request.session['authenticated']
        if is_authenticated:
            user = request.session['user']
            print(user)
            context = {
                'first_name': user['first_name'],
                'last_name': user['last_name'],
                'email': user['email'],
                'creations_number': len(user['creations']),
                'creations': user['creations']
            }
            return render(request, 'profile.html', context)
        else:
            return render(request, 'login.html')
