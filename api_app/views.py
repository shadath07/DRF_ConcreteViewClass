# Concrete view class

from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView, UpdateAPIView,DestroyAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    

# class StudentRetrieve(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
# class StudentUpdate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
    
# class StudentDestroy(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# This is the combination for the concrete view class 

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# class StudentRetrieveUpdate(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    
# class StudentRetrieveDestroy(RetrieveDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
