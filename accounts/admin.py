# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser

# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display  = ["username", "first_name", "last_name", "phone", "is_staff", "created_at"]
#     list_filter   = ["is_staff", "is_superuser", "is_active"]
#     search_fields = ["username", "phone", "first_name", "last_name"]
#     ordering      = ["-created_at"]
#     fieldsets = (
#         (None,                  {"fields": ("username", "password")}),
#         ("Shaxsiy ma'lumotlar", {"fields": ("first_name", "last_name", "phone")}),
#         ("Ruxsatlar",           {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
#         ("Sanalar",             {"fields": ("last_login",)}),
#     )
#     add_fieldsets = (
#         (None, {
#             "classes": ("wide",),
#             "fields": ("username", "phone", "first_name", "last_name", "password1", "password2", "is_staff"),
#         }),
#     )
