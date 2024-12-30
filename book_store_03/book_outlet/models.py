from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Book(models.Model): # table name will be books in the database
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) # rating should be between 1 and 5  
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False) # default value is False
    slug = models.SlugField(default="", null=False, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)
    

    def __str__(self):
        # Following code is used to display the title and rating of the book in the console
        return f"Title: {self.title}, Rating: {self.rating}, Author: {self.author}, Bestselling: {self.is_bestselling}"