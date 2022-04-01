from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StudentTable
from .serializers import StudentSerializer

'''Home Page'''
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

''' Create a student '''
@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({'status':200, 'data':serializer.data})


''' Update a student'''
@api_view(['PUT'])
def update_student(request,id):
    result = StudentTable.objects.get(id=id)
    serializer = StudentSerializer(data=request.data,instance=result)
    if serializer.is_valid():
        serializer.save()
    return Response({'status':200, 'data':serializer.data})

''' Delete a student '''

@api_view(['DELETE'])
def delete_student(request,del_id):
    del_res = StudentTable.objects.get(id=del_id)
    del_res.delete()
    return Response({'status': 200, 'message': 'Student id {} Record deleted successfully!'.format(del_id)})









