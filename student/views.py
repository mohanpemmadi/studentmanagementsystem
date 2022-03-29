from rest_framework.decorators import api_view
from rest_framework.response import Response

# home page

@api_view(['GET'])
def home(request):
    return Response({'status':200,'message':'Hello Everyone, Welcome to Student Home Page!'})

@api_view(['GET'])
def about(request):
    return Response({'status':200,'message':'Hello Everyone, Welcome to Student About Page!'})