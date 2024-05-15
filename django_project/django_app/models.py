from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'
    

class Book(models.Model):
    title = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)#tell django that null is OK

    def __str__(self):
        return f'{self.title}: Author = {self.author}'