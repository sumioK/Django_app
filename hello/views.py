from django.shortcuts import render
from .models import Friend

def index(request):
  data = Friend.objects.all()
  params = {
    'title': 'Hello',
    'message': 'all friends.',
    'data': data,
  }
  return render(request, 'hello/index.html', params)

# class HelloView(TemplateView):
#   def __init__(self):
#     self.params = {
#       'title': 'Hello',
#       'message': 'your data:',
#       'form': HelloForm()
#     }

#   def get(self, request):
#     return render(request, 'hello/index.html', self.params)

#   def post(self, request):
#     msg = 'あなたは、<b>{}さんです。<br>メールアドレスは<b>{}ですね。'.format(request.POST['name'], request.POST['mail'])
#     self.params['message'] = msg
#     self.params['form'] = HelloForm(request.POST)
#     return render(request, 'hello/index.html', self.params)