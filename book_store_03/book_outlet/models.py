from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=9)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"
    
    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model): # table name will be books in the database
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, related_name="author")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        # Following code is used to display the title and rating of the book in the console and admin panel
        return self.full_name()

class Book(models.Model): # table name will be books in the database
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) # rating should be between 1 and 5  
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books") # if author is deleted, all books by that author will also be deleted. 
    is_bestselling = models.BooleanField(default=False) # default value is False
    slug = models.SlugField(default="", blank=True,null=False, unique=True, db_index=True)
    published_countries = models.ManyToManyField("Country", related_name="books")

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})
    

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Book, self).save(*args, **kwargs)
    

    def __str__(self):
        # Following code is used to display the title and rating of the book in the console and admin panel
        return f"Title: {self.title}, Rating: {self.rating}, Author: {self.author}, Bestselling: {self.is_bestselling}"
    

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"Name: {self.name}, Code: {self.code}"
    
    
    class Meta:
        verbose_name_plural = "Countries"    