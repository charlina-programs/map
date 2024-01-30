from django.db import models


# Create your models here.


class Business(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location_lat = models.DecimalField(max_digits=9, decimal_places=6)
    location_lon = models.DecimalField(max_digits=9, decimal_places=6)
    business_image = models.ImageField(upload_to='business_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Review(models.Model):

    business = models.ForeignKey('Business', on_delete=models.CASCADE)  # Use quotes around the model name
    rating = models.PositiveIntegerField()
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Marker(models.Model):
    location_lat = models.DecimalField(max_digits=9, decimal_places=6)
    location_lon = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField()