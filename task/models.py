from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)

    def __str__(self):
        return self.name
