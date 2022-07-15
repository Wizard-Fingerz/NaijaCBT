from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

DEPARTMENT_CHOICES = [
        ("SCIENCE", "SCIENCE"),
        ("ART AND HUMANITY", "ART AND HUMANITY"),
        ("COMMERCIAL", "COMMERCIAL"),
    ]
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.png', upload_to='profile_pics')
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    department = models.CharField(max_length=20,choices = DEPARTMENT_CHOICES, default= "SCIENCE")


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
