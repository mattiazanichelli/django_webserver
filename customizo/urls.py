from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name="index"),
    path('form/', views.form_page, name="form"),
    path('help/', views.help_page, name="help"),
    path('downloadPage/', views.download_page, name="download")
]
