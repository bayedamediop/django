from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from rest_framework.decorators import api_view
from .serializers import FileSerializer
from .models import File

class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getfile(request):
    books = File.objects.all()
    #la serrialisation
    serialization = FileSerializer(books,many=True)
    return Response(serialization.data)
#-----------------------------------
@api_view(['GET'])
def getById(request,id):
    book = File.objects.get(id=id)
    serializer = FileSerializer(book)
    return Response(serializer.data)
#-----------------------------------
@api_view(['PUT'])
def updateFille(request,id):
    book = File.objects.get(id=id)
    serializer = FileSerializer(instance = book, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
#------------------------------------
@api_view(['DELETE'])
def deleteFile(requeqt,id):
     book = File.objects.get(id=id)
     book.delete()
     return Response("File supprimé!!!")
    