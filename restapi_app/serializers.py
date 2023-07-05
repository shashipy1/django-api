from rest_framework import serializers
from restapi_app.models import User, Student, Teacher


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_level']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = '__all__'
