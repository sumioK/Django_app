from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.db.models import Q, Count, Sum, Avg, Min, Max 
from django.core.paginator import Paginator
from .models import Friend, Message
from .forms import FriendForm, FindForm, CheckForm, MessageForm

def index(request, num=1):
  data = Friend.objects.all()
  page = Paginator(data, 3)
  params = {
    'title': 'hello',
    'message': '',
    'data': page.get_page(num)
  }
  return render(request, 'hello/index.html', params)

# create model
def create(request):
  if request.method == 'POST':
    obj = Friend()
    friend = FriendForm(request.POST, instance=obj)
    friend.save()
    return redirect(to='/hello')
  params = {
    'title': 'Hello',
    'form': FriendForm(),
  }
  return render(request, 'hello/create.html', params)

def edit(request, num):
  obj = Friend.objects.get(id=num)
  if request.method == 'POST':
    friend = FriendForm(request.POST, instance=obj)
    friend.save()
    return redirect(to='/hello')
  params = {
    'title': 'Hello',
    'id': num,
    'form': FriendForm(instance=obj),
  }
  return render(request, 'hello/edit.html', params)

def delete(request, num):
  friend = Friend.objects.get(id=num)
  if request.method == "POST":
    friend.delete()
    return redirect(to='/hello')
  params = {
    'title': 'Hello', 
    'id': num,
    'obj': friend,
  }
  return render(request, 'hello/delete.html', params)

class FriendList(ListView):
  model = Friend

class FriendDetail(DetailView):
  model = Friend

def find(request):
  if(request.method == 'POST'):
    form = FindForm(request.POST)
    find = request.POST['find']
    list = find.split()
    data = Friend.objects.all()[int(list[0]):int(list[1])]
    msg = 'Result: ' + str(data.count())
  else:
    msg = 'serch words...'
    form = FindForm()
    data = Friend.objects.all()
  params={
    'title': 'Hello',
    'message': msg,
    'form': form,
    'data': data,
  }
  return render(request, 'hello/find.html', params)

def check(request):
  params = {
    'title' : 'Hello',
    'message' : 'check validation.',
    'form': FriendForm(),
  }
  if request.method == 'POST':
    obj = Friend()
    form = FriendForm(request.POST, instance=obj)
    params['form'] = form
    if form.is_valid():
      params['message'] = 'OK!'
    else:
      params['message'] = 'no good.'
  return render(request, 'hello/check.html', params)

def message(request, page=1):
  if request.method == 'POST':
    obj = Message()
    form = MessageForm(request.POST, instance=obj)
    form.save()
  data = Message.objects.all().reverse()
  paginator = Paginator(data, 5)
  params = {
    'title': 'Message',
    'form': MessageForm(),
    'data': paginator.get_page(page),
  }
  return render(request, 'hello/message.html', params)