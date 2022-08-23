from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name="index"),
    path('create/', views.create_page, name="create"),
    path('guide/', views.guide_page, name="guide"),
    path('login/', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),
    path('mycubus/', views.profile_page, name="profile"),
    path('download/', views.download_page, name="download")
]
