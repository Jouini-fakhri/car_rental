# car_rental/models.py
from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(choices=[('normal', 'Normal'), ('luxury', 'Luxury')], max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    return_date = models.DateField()
    car_image = models.ImageField(upload_to='car_images/', null=True, blank=True)
   
    def __str__(self):
        return f"{self.brand} {self.model}"

    class Meta:
        app_label = 'car_rental'
