from django.urls import path
from .views import *

urlpatterns = [
    path('', InstructorListView.as_view()),
    path('<int:pk>/', InstructorDetailView.as_view()),

    path('create/', InstructorCreateView.as_view()),
    path('<int:pk>/update/', InstructorUpdateView.as_view()),
    path('<int:pk>/delete/', InstructorDeleteView.as_view()),
]