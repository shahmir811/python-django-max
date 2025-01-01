from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
    
    class Meta:
        verbose_name_plural = "Authors"
    
class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    slug = models.SlugField(default="", blank=True,null=False, unique=True) # db_index=True is applied by default
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField('Tag', related_name="posts")

    def __str__(self):
        return self.title

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption