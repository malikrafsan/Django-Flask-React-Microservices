from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

class HomeView(APIView):
   permission_classes = (IsAuthenticated, )
   def get(self, request):
      content = {
        'message': 'Welcome to the Home Page!'
      }
      return Response(content, headers={'Access-Control-Allow-Origin': 'http://localhost:5173'})

class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):          
        try:
          refresh_token = request.data["refresh_token"]
          token = RefreshToken(refresh_token)
          token.blacklist()
          return Response(status=status.HTTP_205_RESET_CONTENT, headers={'Access-Control-Allow-Origin': 'http://localhost:5173'})
        except Exception as e:
          return Response(status=status.HTTP_400_BAD_REQUEST, headers={'Access-Control-Allow-Origin': 'http://localhost:5173'})
