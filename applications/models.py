from django.db import models

# Create your models here.


class Application(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=100)

    def add_key(self):
        pass