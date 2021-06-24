from django.db.models import fields
from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    def validate_password(self, value):
        return make_password(value)
    
    class Meta:
        model = User
        fields = "__all__"

