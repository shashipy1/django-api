from django.db import models
from django.contrib.auth.models import AbstractUser, Group,Permission

# Create your models here.

class User(AbstractUser):
    USER_LEVEL_CHOICES = [
        ('superadmin', 'Super Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='auth_users',  # Add a custom related_name
        related_query_name='user'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='auth_users',  # Add a custom related_name
        related_query_name='user'
    )
    user_level = models.CharField(max_length=20, choices=USER_LEVEL_CHOICES)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # Add other fields specific to the student model


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    students = models.ManyToManyField(Student)
    # Add other fields specific to the teacher model