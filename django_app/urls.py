from django.contrib import admin
from django.urls import path
import hello.views as hello
urlpatterns = [
    path("admin/", admin.site.urls),
    path('hello/', hello.index),
]
