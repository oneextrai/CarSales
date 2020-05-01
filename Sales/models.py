from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=250)
    year = models.CharField(max_length=5)
    price = models.CharField(max_length=25, null=True)
    mileage = models.CharField(max_length=10)
    body_style = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=25)
    description = models.TextField()
    photos = models.TextField()
    is_classic = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.make} {self.model}"

class Classic(Car):
    def __str__(self):
        return f'{self.make} {self.model}'