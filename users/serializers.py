from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User
from rest_framework.serializers import ModelSerializer

from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode



User = get_user_model()


#Resister serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True) 
    id_number = serializers.CharField(max_length=13)

    class Meta:
        model = User
        fields = ('username', 'email', 'id_number', 'password', 'confirm_password')

    def validate_id_number(self, value): 
        if User.objects.filter(id_number=value).exists():
            raise serializers.ValidationError("This id number address is already registered.")
        if not value.isdigit() or len(value) != 13: 
            raise serializers.ValidationError("ID number must be a valid 13-digit South African ID.") 
        return value
    
    # def validate_email(self, value):
    #     if User.objects.filter(email=value).exists():
    #         raise serializers.ValidationError("This email address is already registered.")
    #     return value

    
    def validate(self, data): 
        # Password confirmation 
        if data['password'] != data['confirm_password']: 
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."}) 
        return data

    def create(self, validated_data): 
        validated_data.pop('confirm_password') 
        user = User.objects.create_user( username=validated_data['username'], 
            email=validated_data['email'], 
            id_number=validated_data['id_number'], 
            password=validated_data['password'] 
        ) 
        return user


#Serializer for changing password
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
