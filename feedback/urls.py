from django.urls import path
from .views import FeedbackListCreateView, FeedbackRetrieveUpdateDestroyView

urlpatterns = [
    path('feedback/', FeedbackListCreateView.as_view(), name='feedback-list-create'),
    path('feedback/<int:pk>/', FeedbackRetrieveUpdateDestroyView.as_view(), name='feedback-detail'),
]