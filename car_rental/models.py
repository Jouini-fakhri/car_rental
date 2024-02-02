# car_rental/models.py
from django.db import models
from PIL import Image

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    #car_image = models.ImageField(upload_to='car_images/', blank=True, null=True)
    category = models.CharField(max_length=100, choices=[('Normal', 'Normal'), ('Luxury', 'Luxury')])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    return_date = models.DateField()
    car_image = models.ImageField(upload_to="images/")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    class Meta:
        app_label = 'car_rental'
        
"""
        # Resize the uploaded image to a thumbnail
        if self.car_image:
            img = Image.open(self.car_image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.car_image.path)
"""
    
