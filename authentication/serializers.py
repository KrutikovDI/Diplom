from rest_framework import serializers
from authentication.models import Users

# class UsersSerializer(serializers.Serializer):
#     fullName = serializers.CharField()
#     login = serializers.CharField()
#     email = serializers.EmailField()
#     password = serializers.CharField()

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['fullName', 'login', 'email', 'password', 'admin']