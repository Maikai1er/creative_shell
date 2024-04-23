from django.db import models


# Create your models here.
class CulturalHeritage(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    # description = models.TextField()
    # source_link = models.URLField()
    # image = models.ImageField(upload_to='cultural_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
