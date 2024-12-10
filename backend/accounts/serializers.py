from rest_framework import serializers
from .models import User, BusinessUser, ClientUser, Store

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'account_type']

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id','name', 'location']

class BusinessUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    store = StoreSerializer()

    class Meta:
        model = BusinessUser
        fields = ['id', 'user', 'store', 'admin']

class ClientUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ClientUser
        fields = ['id', 'user']
