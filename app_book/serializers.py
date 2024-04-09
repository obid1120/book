from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author")
    genre = serializers.CharField(source="get_genre_display")

    class Meta:
        model = Book
        fields = (
            'name',
            'author_name',
            'price',
            'genre',
        )