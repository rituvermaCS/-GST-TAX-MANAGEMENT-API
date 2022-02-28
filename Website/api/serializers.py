from rest_framework import serializers
from django.contrib.auth.models import User


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','first_name','last_name','is_superuser','is_staff','is_active','date_joined','last_login')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name','last_name','is_superuser','is_staff','is_active','date_joined','last_login')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['first_name'], validated_data['last_name'], validated_data['is_superuser'], validated_data['is_staff'], validated_data['is_active'], validated_data['date_joined'], validated_data['last_login'])

        return user

class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
       
        instance.username = validated_data['username']
        instance.save()
        return instance

