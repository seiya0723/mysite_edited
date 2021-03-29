from django.shortcuts import render
from django.http import HttpResponse
from django.template import context, loader

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin



"""
def top(request):
    return render(request, 'mysite/top.html')
"""

#ビューにLoginRequiredMixinを引数に指定することで、未ログインの場合はログインページに遷移させる。ログイン済みの場合はそのまま表示
class TopView(View):
#class TopView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):

        #リクエストオブジェクトの中にuserオブジェクトがある。これがユーザーモデル。
        #.idでユーザーのIDを参照できる。認証済みユーザーが投稿した時、誰が投稿したかを記録するときはこのユーザーIDを同時に保存

        print(request.user)
        print(request.user.username)
        print(request.user.id)
        
        return render(request, 'mysite/top.html')

top = TopView.as_view()
