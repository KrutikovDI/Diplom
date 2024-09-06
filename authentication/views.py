from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from authentication.models import Users

# Create your views here.
def chat_enter(request):
    message = 'вы вошли в систему'
    return HttpResponse(message)

def users_list(request):
    users = Users.objects.all()
    return HttpResponse(users)

def user_login(request, user_login):
    user = get_object_or_404(Users, login=user_login)
    return HttpResponse(user)