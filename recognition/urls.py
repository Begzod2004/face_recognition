from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('recognize/', views.face_recognition, name='face_recognition'),
]
