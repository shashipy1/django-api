from django.shortcuts import render
from rest_framework import viewsets
from restapi_app.models import User, Student, Teacher
from restapi_app.serializers import UserSerializer, StudentSerializer, TeacherSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
