from django.urls import path
from . import views

urlpatterns = [
  path('my_name_is_<nickname>.I_am_<int:age>_years_old.',views.index, name='index'),
]