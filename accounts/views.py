from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer, LogoutSerializer, ProfileSerializer
from rest_framework import generics, status
from .models import CustomUser

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = CustomUser.objects.get(phone_number=request.data['phone_number'])
        refresh = RefreshToken.for_user(user)

        response.data = {
            "user": response.data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return response

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "phone_number": user.phone_number,
                "first_name": user.first_name,
            }
        }, status=status.HTTP_200_OK)

class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Muvaffaqiyatli chiqildi"},
                        status=status.HTTP_200_OK)
    
class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()

    def get_object(self):
        obj = super().get_object()

        # Faqat o'z profilini ko‘rishga ruxsat
        if obj != self.request.user:
            raise PermissionError("Siz boshqa foydalanuvchi profilini ko‘ra olmaysiz")

        return obj