from django.urls import path
from .views import HelloView

urlpatterns = [
  path(r'', HelloView.as_view(), name='index'),
]