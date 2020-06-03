from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Author, Book, User, Lend
from .serializers import BookSerializer, UserSerializer, LendSerializer, \
    AuthorSerializer, createBookSerializer, createLendSerializer
import json
from django.core import serializers


# Create your views here.


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def lend_list(request):
    if request.method == 'GET':
        lends = Lend.objects.all()
        serializer = LendSerializer(lends, many=True)
        return JSONResponse(serializer.data, status=200)
    elif request.method == 'POST':

        data = JSONParser().parse(request)

        book = Book.objects.get(id=data['book_id']['id'])

        print(book)

        author = Author.objects.get(id=data['book_id']['author']['id'])

        print(author)

        data['book_id']['author'] = author

        data['book_id'] = book

        createSerializer = createLendSerializer(data=data)

        # print(createSerializer)
        if createSerializer.is_valid():
            createSerializer.save()
            return JSONResponse(createSerializer.data, status=201)
        return JSONResponse(createSerializer.errors, status=400)


@csrf_exempt
def lend_detail(request, pk):
    try:
        lend = Lend.objects.get(pk=pk)
    except Lend.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LendSerializer(lend)
        return JSONResponse(serializer.data, status=200)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LendSerializer(lend, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        lend.delete()
        return HttpResponse(status=204)


@csrf_exempt
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = createBookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
