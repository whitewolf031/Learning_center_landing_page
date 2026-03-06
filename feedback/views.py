from rest_framework import generics, permissions
from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackListCreateView(generics.ListCreateAPIView):
    queryset = Feedback.objects.filter(approved=True).select_related('course')
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(
            name=self.request.user.get_full_name(),
            role=getattr(self.request.user, 'role', ''),
            image=getattr(self.request.user, 'profile_image', None)
        )

class FeedbackRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all().select_related('course')
    serializer_class = FeedbackSerializer

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]