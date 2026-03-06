from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken
import re
from .models import CustomUser

User = get_user_model()

def validate_user_password(password):
    min_len = 8
    if len(password) < min_len:
        raise serializers.ValidationError(f"Parol kamida {min_len} belgidan iborat bo'lishi kerak.")
    if not re.match(r"^[A-Za-z0-9]+$", password):
        raise serializers.ValidationError("Parol faqat raqamlar va harflardan iborat bo'lishi kerak.")
    if not re.search(r"[A-Za-z]", password) or not re.search(r"\d", password):
        raise serializers.ValidationError("Parol kamida bitta harf va bitta raqamdan iborat bo'lishi kerak")

    return password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_user_password])
    password2 = serializers.CharField(write_only=True, label="Parolni tasdiqlash")

    class Meta:
        model = User
        fields = (
            "phone_number",
            "password",
            "password2",
            "first_name",
            "last_name"
        )

    def validate_phone_number(self, value):
        if not value.startswith("+998"):
            value = "+998" + value.replace("+998", "").replace(" ", "")
        if len(value) != 13 or not value[4:].isdigit():
            raise serializers.ValidationError("Telefon raqami +998XXXXXXXXX formatida bo‘lishi kerak")
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Bu telefon raqami allaqachon ro‘yxatdan o‘tgan")
        return value

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password2": "Parollar mos emas!"})
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        password = validated_data.pop("password")

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        phone = data["phone_number"]
        password = data["password"]

        # +998 formatini to‘g‘rilaymiz
        if not phone.startswith("+998"):
            phone = "+998" + phone.replace("+998", "").replace(" ", "")

        try:
            user = User.objects.get(phone_number=phone)
        except User.DoesNotExist:
            raise serializers.ValidationError("Bunday telefon raqami topilmadi")

        if not user.check_password(password):
            raise serializers.ValidationError("Noto‘g‘ri parol")

        if not user.is_active:
            raise serializers.ValidationError("Hisob faol emas")

        data["user"] = user
        return data

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()   # tokenni blacklistga qo‘shadi
        except Exception as e:
            raise serializers.ValidationError("Noto‘g‘ri yoki allaqachon ishlatilgan token")
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "phone_number", "first_name", "last_name"]