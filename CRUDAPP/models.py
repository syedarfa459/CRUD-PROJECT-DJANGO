from django.db import models

# Create your models here.


class Car(models.Model):

    name = models.CharField(max_length=50)
    color = models.CharField(max_length=15)
    car_number = models.CharField(max_length=20)
    reg_city = models.CharField(max_length=50)

    def __str__(self):
        return self.name

