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
  api_key = os.getenv('API_KEY_BLOG')

  def get(self, request):
      try:
        username = request.user.username

        response = requests.get(
          f'http://localhost:5001/blog?username={username}', 
          headers={
            'x-api-key': BlogView.api_key
          })
        
        return Response(response.json(), headers={'Access-Control-Allow-Origin': 'http://localhost:5173'})
      except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)
  
  def post(self, request):
      try:
        username = request.user.username
        title = request.data['title']
        content = request.data['content']

        response = requests.post(
          'http://localhost:5001/blog', 
          json={
            'username': username,
            'title': title,
            'content': content
          },
          headers={
            'x-api-key': BlogView.api_key
          })
        
        return Response(response.json())
      except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)
