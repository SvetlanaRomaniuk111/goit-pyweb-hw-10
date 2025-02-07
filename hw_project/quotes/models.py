from django.db import models


# Create your models here.

class Author(models.Model):
    fullname = models.CharField(max_length=120, unique=True)
    born_date = models.CharField(max_length=50)
    born_location = models.CharField(max_length=120)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    mongo_id = models.CharField(max_length=24, unique=True, null=True,
                                blank=True)

    def __str__(self):
        return self.fullname


class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None,
                               null=True)
    quote = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'"{self.quote}" - {self.author}'
