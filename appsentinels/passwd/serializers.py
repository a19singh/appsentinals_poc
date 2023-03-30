from .models import PlatformUser

from django.contrib.auth import password_validation
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class PlatformUserSerializer(serializers.ModelSerializer):
    """
    Serializer to handle CRUD Operations for User model
    """

    def validate_passwd(self, value):
        password_validation.validate_password(value, self.instance)
        return value


    class Meta:
        model = PlatformUser
        fields = '__all__'
        read_only_fields = ('cdate', )

    def create(self, validated_data):
        """
        Create method to create user
        """
        validated_data['passwd'] = make_password(
            validated_data['passwd'], 'appsentinals', 'pbkdf2_sha256'
        )
        user_instance = PlatformUser.objects.create(**validated_data)
        return user_instance


class PlatformUserListSerializer(serializers.ModelSerializer):
    """
    Serializer to handle CRUD Operations for User model
    """

    def validate_passwd(self, value):
        password_validation.validate_password(value, self.instance)
        return value


    class Meta:
        model = PlatformUser
        exclude = ('passwd',)
        read_only_fields = ('cdate', )
