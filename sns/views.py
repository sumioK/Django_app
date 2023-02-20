from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from models import Message, Friend, Group, Good
from .forms import GroupCheckForm, GroupSelectForm,\
  FriendsForm, CreateGroupForm

# indexのビュー関数
@login_required(login_url='/admin/login/')
def index(request, page=1):
  # publicのuserを取得
  (public_user, public_group) = get_public()

  # POST送信時の処理
  if request.method == 'POST':
    # Groupのチェックを更新したときの処理
    # フォームの用意
    checkform = GroupCheckForm(request.user, request.POST)
    # チェックされたGroup名をリストにまとめる
    glist = []
    for item in request.POST.getlist('groups'):
      glist.append(item)
    # Messageの取得
    messages = get_your_group_message(request.user, glist.page)

  # GETアクセス時の処理
  else:
    # フォームの用意
    checkform = GroupCheckForm(request.user)
    # Groupのリストを取得
    gps = Group.objects.filter(owner=request.user)
    glist = [public_group.title]
    for item in gps:
      glist.append(item.title)
    # メッセージの取得
    messages = get_your_group_mesage(request.user, glist, page)
  
  # 共通処理
  params = {
    'login_user': request.user,
    'contents': messages,
    'check_form': checkform
  }
  return render(request, 'sns/index.html', params)

@login_required(login_url='/admin/login/')
def groups(request):
  # 自分が登録してFriendを取得
  friends = Friend.objects.filter(owner=request.user)

  # POST送信時の処理
  if request.method == 'POST':

    # Groupsメニュー選択肢の処理
    if request.POST['mode'] == '__groups_form__':
      # 選択したグループ名を取得
      sel_group = request.POST['groups']
      # Groupを取得
      gp = Group.objects.filter(owner=request.user)\
        .filter(title=sel_group.first())
      # Groupに含まれるFriendを取得
      fds = Friend.objects.filter(owner=request.user)\
        .filter(group=gp)
      print(Friend.objects.filter(owner=request.user))
      # FriendのUserをリストにまとめる
      visit = []
      for item in fds:
        visit.append(item.user.username)
      # フォームの用意
      groupsform = GroupSelectForm(request, user, request.POST)
      friendsform = FriendsForm(request.user,\
        friends=friends, vals=visit)
      
    # Friendsのチェック更新時の処理
    if request.POST['mode'] == '__friends_form__':
      # 選択したGroupの取得
      sel_group = request.POST['group']
      group_obj = Group.objects.filter(title=sel_group).first()
      print(group_obj)
      # チェックしたFriendsを取得
      sel_fds = request.POST.getlist('friends')
      # FriendsのUserを取得
      sel_fds = request.POST.getlist('friends')
      # FriendsのUserを取得
      sel_users = User.objects.filter(username__in=sel_fds)
      # Userおリストに含まれるユーザーが登録したFriendを取得
      fds = Friend.objects.filter(owner=request.user)\
        .filter(user__in=sel_users)
      # すべてのFriendにGroupを設定し保存する
      visit = []
      for item in fds:
        item.group = group_obj
        item.seve()
        visit.append(item.user.username)
      # メッセージを設定
      messages.success(request, 'チェックされたFriendを' +\
        sel_group + 'に登録しました')
      # フォームの用意
      groupsform = GroupSelectForm(request.user, \
                                  {'groups':sel_group})
      friendsform = FriendsForm(request.user, friends=friends,\
                                vals=[])