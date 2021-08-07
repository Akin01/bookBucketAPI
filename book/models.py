from django.db import models

class bookType(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre

class bookList(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=30)
    year = models.IntegerField()
    publisher = models.CharField(max_length=50)
    genre = models.ManyToManyField(bookType, related_name="booktype")

    def __str__(self):
        return self.title



