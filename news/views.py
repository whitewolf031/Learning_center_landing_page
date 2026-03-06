from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import News
from .serializers import NewsListSerializer, NewsDetailSerializer, NewsCreateUpdateSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()

    def get_permissions(self):

        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get_serializer_class(self):

        if self.action == 'list':
            return NewsListSerializer          
        elif self.action == 'retrieve':
            return NewsDetailSerializer        
        return NewsCreateUpdateSerializer      

    def perform_create(self, serializer):

        serializer.save(author=self.request.user)