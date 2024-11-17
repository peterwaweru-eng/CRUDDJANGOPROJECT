from django.db import models
from django.template.defaultfilters import title


# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()


    def __str__(self):
        return self.name


class Category(models.Model):
    name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

class Blogpost(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField()
    published_date=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
