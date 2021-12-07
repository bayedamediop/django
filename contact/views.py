from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContactSerializers
from .models import Contact

# Create your views here.
@api_view(['GET'])
def allContact(request):
    contact = Contact.objects.all()
    #la serrialisation
    serialization = ContactSerializers(contact,many=True)
    return Response(serialization.data)

#-----------------------------------

#-----------------------------------
@api_view(['GET'])
def getById(request,id):
    book = Contact.objects.get(id=id)
    serializer = ContactSerializers(book)
    return Response(serializer.data)
#-----------------------------------
@api_view(['POST'])
def addContact(request):
    serializer = ContactSerializers(data = request.data, many = True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
#-----------------------------------
@api_view(['PUT'])
def updateContact(request,id):
    book = Contact.objects.get(id=id)
    serializer = ContactSerializers(instance = book, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
#------------------------------------
@api_view(['DELETE'])
def deleteContact(requeqt,id):
     book = Contact.objects.get(id=id)
     book.delete()
     return Response("Contact supprimé!!!")
    

