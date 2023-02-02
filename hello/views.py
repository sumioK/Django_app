from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend
from .forms import HelloForm

# def index(request):
#   params = {
#     'title': 'Hello',
#     'message': 'all friends.',
#     'form': HelloForm,
#     'data': [],
#   }
#   if(request.method == 'POST'):
#     num=request.POST['id']
#     item = Friend.objects.get(id=num)
#     params['data'] = [item]
#     params['form'] = HelloForm(request.POST)
#   else:
#     params['data'] = Friend.objects.all()
#   return render(request, 'hello/index.html', params)
def index(request):
  num = Friend.objects.all().count()
  first = Friend.objects.all().first()
  last = Friend.objects.all().last()
  data = [num, first, last]
  params = {
    'title': 'Hello',
    'data': data
  }
  return render(request, 'hello/index.html', params)