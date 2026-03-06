from rest_framework import serializers
from .models import News


class NewsListSerializer(serializers.ModelSerializer):

    author_name = serializers.CharField(source='author.get_full_name', read_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'image', 'author_name', 'created_at']


class NewsDetailSerializer(serializers.ModelSerializer):

    author_name = serializers.CharField(source='author.get_full_name', read_only=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'image', 'author_name', 'created_at', 'updated_at']


class NewsCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['id', 'title', 'content', 'image']
