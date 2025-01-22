from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length = 200)
    recipe_description = models.TextField(blank=True)
    recipe_image = models.ImageField(upload_to='recipe/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200,unique=True,null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.recipe_name)
        super(Recipe, self).save(*args, **kwargs)

    def __name__(self):
        return self.receipe_name
    