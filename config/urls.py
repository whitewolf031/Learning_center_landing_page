from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from feedback.views import FeedbackListCreateView, FeedbackRetrieveUpdateDestroyView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('feedback/', FeedbackListCreateView.as_view(), name='feedback-list-create'),
    path('feedback/<int:pk>/', FeedbackRetrieveUpdateDestroyView.as_view(), name='feedback-detail'),    
]