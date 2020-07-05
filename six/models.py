from django.db import models

# Create your models here.

class Six(models.Model):
    photo = models.ImageField(upload_to="image", blank = True)
    imagename = models.TextField(max_length = 20)
    imageinfo = models.TextField(max_length = 300)
    imageinfo2 = models.TextField(max_length = 300, blank = True)