from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LivreSerializers
from .models import Livre

# Create your views here.
@api_view(['GET'])
def allBooks(request):
    books = Livre.objects.all()
    #la serrialisation
    serialization = LivreSerializers(books,many=True)
    return Response(serialization.data)

#-----------------------------------
@api_view(['GET'])
def getById(request,id):
    book = Livre.objects.get(id=id)
    serializer = LivreSerializers(book)
    return Response(serializer.data)
#-----------------------------------
@api_view(['POST'])
def addBook(request):
    serializer = LivreSerializers(data = request.data, many = True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
#-----------------------------------
@api_view(['PUT'])
def updateBook(request,id):
    book = Livre.objects.get(id=id)
    serializer = LivreSerializers(instance = book, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
#------------------------------------
@api_view(['DELETE'])
def deleteBook(requeqt,id):
     book = Livre.objects.get(id=id)
     book.delete()
     return Response("livre supprimé!!!")
    
