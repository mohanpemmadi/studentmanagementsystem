from rest_framework.serializers import ModelSerializer
from .models import StudentTable

class StudentSerializer(ModelSerializer):
    class Meta:
        model = StudentTable
        fields = '__all__' # ['name','city']

