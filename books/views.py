from django.shortcuts import render
from rest_framework import generics
from books.models import *
from books.serializers import *


class BookListView(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class AuthorListView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()