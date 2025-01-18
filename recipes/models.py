from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length = 200)
    recipe_description = models.TextField(blank=True)
    recipe_image = models.ImageField(upload_to='recipe/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __name__(self):
        return self.receipe_name
    