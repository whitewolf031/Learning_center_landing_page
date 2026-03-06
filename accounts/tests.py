from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CustomUser


class AuthTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser",
            phone="+998901234567",
            password="testpass123",
            first_name="Test",
            last_name="User",
        )
    def test_register_success(self):
        url  = reverse("auth-register")
        data = {
            "username": "newuser",
            "phone": "+998907654321",
            "password": "newpass123",
            "first_name": "New",
            "last_name": "User",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("tokens", response.data)
    def test_register_duplicate_username(self):
        url  = reverse("auth-register")
        data = {"username": "testuser", "phone": "+998909999999", "password": "pass1234"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    def test_login_success(self):
        url  = reverse("auth-login")
        data = {"username": "testuser", "password": "testpass123"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data["tokens"])
    def test_login_wrong_password(self):
        url  = reverse("auth-login")
        data = {"username": "testuser", "password": "wrongpass"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    def test_profile_requires_auth(self):
        url      = reverse("auth-profile")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    def test_profile_authenticated(self):
        self.client.force_authenticate(user=self.user)
        url      = reverse("auth-profile")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "testuser")
