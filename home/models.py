from django.db import models
import django.utils.timezone as datetime
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 200)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(default=datetime.now)

class Car(models.Model):
    name = models.CharField(max_length = 200)
    speed = models.IntegerField(default=50)

    def __str__(self):
        return self.name