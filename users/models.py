from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="user.png", upload_to="profile_pics")
    first_name = models.CharField(max_length=128, default="first name")
    last_name = models.CharField(max_length=128, default="last name")
    address = models.CharField(max_length=256, default="1234 N Main Street")
    city = models.CharField(max_length=128, default="New York")
    country = models.CharField(max_length=128, default="United States")
    postal_code = models.IntegerField(default=12345)
    about = models.TextField(default="A little about me...")
    
    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        # Implement a better method later
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
