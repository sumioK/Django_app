from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Friend
from .forms import HelloForm

def index(request):
  data = Friend.objects.all()
  params = {
    'title': 'Hello',
    'data': data,
  }
  return render(request, 'hello/index.html', params)

# create model
def create(request):
  params = {
    'title': 'Hello',
    'form': HelloForm(),
  }
  if (request.method == 'POST'):
    name = request.POST['name']
    mail = request.POST['mail']
    gender = 'gender' in request.POST
    age = int(request.POST['age'])
    birth = request.POST['birthday']
    friend = Friend(name=name, mail=mail, gender=gender, age=age, birthday=birth)
    friend.save()
    return redirect(to='/hello')
  return render(request, 'hello/create.html', params)