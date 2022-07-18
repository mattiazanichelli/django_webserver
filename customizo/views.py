from django.shortcuts import render


# Create your views here.
def index_page(request):
    return render(request, 'index.html')


def form_page(request):
    return render(request, 'form.html')


def help_page(request):
    return render(request, 'help.html')


