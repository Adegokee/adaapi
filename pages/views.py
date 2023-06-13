from django.shortcuts import render
from pages.serializer import TodoSerializer
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from pages.models import Todo
import requests

# Create your views here.
@api_view(['POST'])
def createtodo(request):
    record =TodoSerializer(data=request.data)
    if record.is_valid():
        record.save()
    return Response(record.data)


@api_view(['GET'])
def alltodo(request):
    record=Todo.objects.all()
    info=TodoSerializer(record, many=True)
    return Response(info.data)


@api_view(['DELETE'])
def tododelete(request, id):
    record=Todo.objects.get(id=id)
    record.delete()
    return Response('Todo deleted successfully')

@api_view(['PUT'])
def edittodo(request, id):
    record=Todo.objects.get(id=id)
    info=TodoSerializer(data=request.data, instance=record)
    if info.is_valid():
        info.save()
        return Response('update successfully')



def index(request):
    url=requests.get('http://localhost:8000/api/v1/alltodo')
    data=url.json()
    context={'data': data}
    return render(request, 'index.html', context)
