from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name="index"),
    path('form/', views.form_page, name="form"),
    path('guide/', views.guide_page, name="guide"),
    path('download/', views.download_page, name="download")
]
