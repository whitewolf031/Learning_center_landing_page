from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model  = CustomUser
        fields = ["username", "first_name", "last_name", "phone", "password"]
    def create(self, validated_data):
        return CustomUser.objects.create_user(
            username   = validated_data["username"],
            phone      = validated_data["phone"],
            password   = validated_data["password"],
            first_name = validated_data.get("first_name", ""),
            last_name  = validated_data.get("last_name", ""),
        )

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Username yoki parol noto'g'ri.")
        if not user.is_active:
            raise serializers.ValidationError("Foydalanuvchi bloklangan.")
        data["user"] = user
        return data

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CustomUser
        fields = ["id", "username", "first_name", "last_name", "phone", "created_at"]
        read_only_fields = ["id", "username", "created_at"]
