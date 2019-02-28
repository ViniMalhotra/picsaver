from django.db import models
from django.urls import reverse

# Create your models here.
class Album(models.Model):
    placeName = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000, default="one")
    picture = models.FileField(default='settings.MEDIA_ROOT/logos/anonymous.jpg')



    def get_absolute_url(self):
        return reverse('picSaver:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.placeName

