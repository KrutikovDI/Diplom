"""
URL configuration for myCloud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

# from authentication.views import chat_enter, users_list, UserView
from authentication.views import chat_enter
from authentication.views import UsersViewSet

r = DefaultRouter()
r.register('RegistrationUser', UsersViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('enter/', chat_enter, name='enter'),
    # path('users/', users_list, name='listing'),
    # path('user/<str:user_login>/', user_login, name='login')
    # path('user/<fullName>/', UserView.as_view())
] + r.urls
