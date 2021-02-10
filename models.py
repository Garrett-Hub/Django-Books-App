from django.db import models


# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=60, default="", blank=False, null=False)
    lastName = models.CharField(max_length=60, default="", blank=False, null=False)

    objects = models.Manager()

    def __str__(self):
        return(self.firstName + " " + self.lastName)


class Book(models.Model):
    title = models.CharField(max_length=120, default="", blank=False, null=False, unique=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    year = models.IntegerField()
    description = models.TextField(max_length=255, default="")

    objects = models.Manager()

    def __str__(self):
        return self.title

