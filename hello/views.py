from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend
from django.db.models import QuerySet

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

def __new_str__(self):
  result = ''
  for item in self:
    result += '<tr>'
    for k in item:
      result += '<td>' +str(k) + '=' + str(item[k]) + '</td>'
    result += '</tr>'
  return result

QuerySet.__str__ = __new_str__

def index(request):
  data = Friend.objects.all().values('id', 'name', 'age')
  params = {
    'title': 'Hello',
    'data': data,
  }
  return render(request, 'hello/index.html', params)