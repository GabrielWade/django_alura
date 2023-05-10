from django.urls import path
from galeria.views import index, imagem

urlpatterns = [path("", index), path("imagem/", imagem)]
from django.urls import path
from galeria.views import index, imagem

urlpatterns = [
    path("", index, name="index"),
    path("imagem/", imagem, name="imagem"),
]
