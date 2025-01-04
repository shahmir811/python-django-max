from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

class Review(models.Model):
  user_name = models.CharField(max_length=100)
  review_text = models.TextField()
  ratings = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

  def __str__(self):
    return self.user_name
  