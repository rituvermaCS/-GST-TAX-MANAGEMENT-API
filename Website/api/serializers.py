from rest_framework import serializers
from django.contrib.auth.models import User


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','first_name','last_name','GST','State','Phone','Address','Business_name')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name','last_name','GST','State','Phone','Address','Business_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['first_name'], validated_data['last_name'], validated_data['GST'], validated_data['State'], validated_data['Phone'], validated_data['Address'], validated_data['Business_name'])

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

