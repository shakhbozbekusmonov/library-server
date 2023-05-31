from django.shortcuts import render
from rest_framework import generics
from .models import Books
from .serializers import BookSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class BookListApiView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BookCreateApiView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    # parser_classes = (MultiPartParser, FormParser)


class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer