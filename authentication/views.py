# from django.http import HttpResponse
import json
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ViewSet, ModelViewSet


from authentication.models import Users
from authentication.serializers import UsersSerializer

# def chat_enter(request):
#     message = 'вы вошли в систему'
#     print('вы вошли в систему')
#     return HttpResponse(message)

# def users_list(request):
#     users = Users.objects.all()
#     return HttpResponse(users)

# def user_login(request, user_login):
#     user = get_object_or_404(Users, login=user_login)
#     return HttpResponse(user)

@api_view(['POST'])
def chat_enter(request):
    data = {'сообщение': 'пришел пост запрос'}
    # data_json = request.body.decode('utf-8')
    print(request.body.decode('utf-8'))
    return Response(data)

# @api_view(['GET'])
# def users_list(request):
#     users = Users.objects.all()
#     serializer_user = UsersSerializer(users, many=True)
#     print('получен запрос на users')
#     return Response(serializer_user.data)

# class UserView(ListAPIView):
#     queryset = Users.objects.all()
#     serializer_class = UsersSerializer

class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    filterset_fields = ['fullName', 'password',]