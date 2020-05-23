from django.db import models

from django.urls import reverse

# Create your models here.

class Car(models.Model):
    REDCAR = 'Red Car'
    BLUECAR = 'Blue Car'
    GREENCAR = 'Green Car'
    CAR_COLOR_CHOICES = [
        (REDCAR, 'RedCar'),
        (BLUECAR, 'BlueCar'),
        (GREENCAR,'Green Car'),
    ]
    name = models.CharField(
        max_length=200,
        choices=CAR_COLOR_CHOICES,
        default=REDCAR,)
    # images = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})