from django.db import models

# Create your models here.
class Page(models.Model):
    name=models.CharField(max_length=100)
    website=models.CharField(max_length=256)
    stars=models.DecimalField(max_digits=5,decimal_places=1 , default=0)

    def __str__(self):
        return self.name