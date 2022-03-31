from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StudentTable
from .serializers import StudentSerializer

# home page

@api_view(['GET'])
def home(request):
    return Response({'status':200,'message':'Hello Everyone, Welcome to Student Home Page!!'})

@api_view(['GET'])
def about(request):
    return Response({'status':200,'message':'Hello Everyone, Welcome to Student About Page!!'})

@api_view(['GET'])
def student_list(request):
    result = StudentTable.objects.all()
    list_serializer = StudentSerializer(result,many=True)
    return Response({'status':200,'data':list_serializer.data})

@api_view(['GET'])
def get_student_by_id(request,req_id):
    result = StudentTable.objects.get(id=req_id)
    list_serializer = StudentSerializer(result)
    return Response({'status':200,'data':list_serializer.data})

@api_view(['GET'])
def get_student_by_name(request,name):
    result = StudentTable.objects.get(name=name)
    list_serializer = StudentSerializer(result)
    return Response({'status':200,'data':list_serializer.data})

@api_view(['GET'])
def student_list_filter(request,grade):
    result = StudentTable.objects.filter(grade=grade)
    list_serializer = StudentSerializer(result,many=True)
    return Response({'status':200,'data':list_serializer.data})




