from django import forms
from .models import Message, Group, Friend, Good
from django.contrib.auth.models import User

# Messageのフォーム(未使用)
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['owner', 'group', 'content']

# Groupのフォーム(未使用)
class GroupForm(forms.ModelForm):
    class Meta:
        models = Group
        fields = ['owner', 'title']

# Friendのフォーム(未使用)
class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['owner', 'user', 'group']

# Goodのフォーム(未使用)
class GoodForm(forms.ModelForm):
    class Meta:
        model = Good
        firlds = ['owner', 'message']

