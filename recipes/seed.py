from faker import Faker
fake = Faker()
import requests
from random import randint
from django.core.files.base import ContentFile
from io import BytesIO
from .models import Recipe
from django.contrib.auth.models import User

def seed_recipe(n = 10):
    for _ in range(n):
        # Generate fake image URL (you can use a service like Lorem Picsum)
        image_url = f"https://picsum.photos/200/300?random={randint(1, 1000)}"  # Random image

        # Fetch the image from the URL
        response = requests.get(image_url)
        img = BytesIO(response.content)  # Convert the image into a format Django can save

        user_objs = User.objects.all()
        user = user_objs[randint(0, len(user_objs) - 1)]

        recipe = Recipe.objects.create(
            user=user,
            recipe_name=fake.name(),
            recipe_description=fake.text(),
            created_at=fake.date_time_this_year()
        )

        # Save the image to the recipe instance
        recipe.recipe_image.save(f'{fake.word()}.jpg', ContentFile(img.read()), save=True)
        recipe.save()