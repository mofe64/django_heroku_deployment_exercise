from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=40, unique=True, null=False)
    author = models.CharField(max_length=30, null=False)
    pages = models.IntegerField(default=0)
    coverImage = models.ImageField(upload_to='book_covers')
    date_listed = models.DateField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
