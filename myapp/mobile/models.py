from django.db import models

# Create your models here.
class Mobile(models.Model):
    name = models.CharField(max_length=22)
    cost = models.IntegerField()
    location = models.CharField(max_length=11)

    def __str__(self) -> str:
        return self.name

# m1 = Mobile()
