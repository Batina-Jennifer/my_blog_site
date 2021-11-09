from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=200, help_text="plant name")
    picture = models.URLField(max_length=1000)
    rating = models.DecimalField(decimal_places=2, max_digits=4, validators=[MaxValueValidator(5)])
    price = models.CharField(max_length=15, default='')

    def __str__(self):
        return self.name