from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
# Create your views here.

class apiOverview(APIView):
    def get(self,request):
        api_urls = {
            'List': '/task-list/',
            'Detail View': '/task-detail/<str:pk>',
            'Create': '/task-create/',
            'Update': '/task-update/<str:pk>',
            'Delete': '/task-delete/<str:pk>',
            }
        return Response(api_urls)


class taskList(APIView):
    def get(self, request):
        tasks = Task.objects.all().order_by('-id')
        serializer = TaskSerializer(tasks, many = True)
        return Response(serializer.data)

class taskDetail(APIView):
    def get(self, request, pk):
        tasks = Task.objects.get(id = pk)
        serializer = TaskSerializer(tasks, many=False)
        return Response(serializer.data)

class taskCreate(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class taskUpdate(APIView):
    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class taskDelete(APIView):
    def delete(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()

        return Response('Item successfully deleted')
