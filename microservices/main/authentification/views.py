from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth.models import User


class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):          
        try:
          refresh_token = request.data["refresh_token"]
          token = RefreshToken(refresh_token)
          token.blacklist()
          return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
          return Response(status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
   permission_classes = ()
   def post(self, request):
      try:
        username = request.data['username']
        password = request.data['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return Response(status=status.HTTP_201_CREATED)
      except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)
