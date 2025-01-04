from django.db import models


# Create your models here.
class UserProfile(models.Model):
    # image = models.ImageField(upload_to="images/") # Uploads to MEDIA_ROOT/images
    image = models.ImageField(upload_to="images/") # Uploads to MEDIA_ROOT/images
    