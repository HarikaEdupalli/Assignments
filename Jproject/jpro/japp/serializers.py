from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Pro
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email','password']
class ProSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pro
        fields = [ 'id', 'name','price']  