from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import requests
import os


class BlogView(APIView):
  permission_classes = (IsAuthenticated, )
  api_key = os.getenv('API_KEY')

  def get(self, request):
      try:
        username = request.user.username

        response = requests.get(
          f'http://localhost:5000/blog?username={username}', 
          headers={
            'x-api-key': BlogView.api_key
          })
        
        return Response(response.json(), headers={'Access-Control-Allow-Origin': 'http://localhost:5173'})
      except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin': 'http://localhost:5173'})
  
  def post(self, request):
      try:
        username = request.user.username
        title = request.data['title']
        content = request.data['content']

        response = requests.post(
          'http://localhost:5000/blog', 
          json={
            'username': username,
            'title': title,
            'content': content
          },
          headers={
            'x-api-key': BlogView.api_key
          })
        
        return Response(response.json(), headers={'Access-Control-Allow-Origin': 'http://localhost:5173'})
      except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin': 'http://localhost:5173'})
