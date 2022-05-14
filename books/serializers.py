from books.models import *
from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['title_of_genre',]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.full_name')
    genre = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = ['title_of_book', 'genre', 'author']
