from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HomeView(APIView):
   permission_classes = (IsAuthenticated, )

   def get(self, _):
      content = {
          'message': 'Welcome to the Home Page!'
      }
      return Response(content)

