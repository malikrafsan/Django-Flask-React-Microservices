from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status as http_status
import requests
import os


class TaskView(APIView):
  permission_classes = (IsAuthenticated, )
  api_key = os.getenv('API_KEY_TASK')

  def get(self, request):
      try:
        username = request.user.username

        response = requests.get(
            f'http://localhost:5002/task?username={username}',
            headers={
                'x-api-key': TaskView.api_key
            })

        return Response(response.json())
      except Exception as e:
        print(e)
        return Response(status=http_status.HTTP_400_BAD_REQUEST)

  def post(self, request):
      try:
        username = request.user.username
        title = request.data['title']
        description = request.data['description']

        response = requests.post(
            'http://localhost:5002/task',
            json={
                'username': username,
                'title': title,
                'description': description
            },
            headers={
                'x-api-key': TaskView.api_key
            })

        return Response(response.json())
      except Exception as e:
        print(e)
        return Response(status=http_status.HTTP_400_BAD_REQUEST)
      
class TaskDetailView(APIView):
  permission_classes = (IsAuthenticated, )
  api_key = os.getenv('API_KEY_TASK')

  def get(self, request):
      try:
        username = request.user.username
        id = request.data['id']

        response = requests.get(
            f'http://localhost:5002/task/{id}?username={username}',
            headers={
                'x-api-key': TaskDetailView.api_key
            })

        return Response(response.json())
      except Exception as e:
        print(e)
        return Response(status=http_status.HTTP_400_BAD_REQUEST)
      
  def put(self, request):
      try:
        username = request.user.username
        id = request.data['id']
        title = request.data['title']
        content = request.data['description']
        status = request.data['status']

        response = requests.put(
            f'http://localhost:5002/task/{id}?username={username}',
            json={
                'title': title,
                'content': content,
                'status': status
            },
            headers={
                'x-api-key': TaskDetailView.api_key
            })

        return Response(response.json())
      except Exception as e:
        print(e)
        return Response(status=http_status.HTTP_400_BAD_REQUEST)
      
  def delete(self, request):
      try:
        id = request.data['id']
        username = request.user.username

        response = requests.delete(
            f'http://localhost:5002/task/{id}?username={username}',
            headers={
                'x-api-key': TaskDetailView.api_key
            })

        return Response(response.json())
      except Exception as e:
        print(e)
        return Response(status=http_status.HTTP_400_BAD_REQUEST)
