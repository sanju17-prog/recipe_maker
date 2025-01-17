from django.test import TestCase
from django.db import models
# Create your tests here.
class Student(models.Model):
    name = models.CharField(max_length=255)