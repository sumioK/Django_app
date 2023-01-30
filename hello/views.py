from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  params = {
    'title': 'Hello/Index',
    'msg': 'これはサンプルで作ったページです'
  }
  return render(request, 'hello/index.html', params)