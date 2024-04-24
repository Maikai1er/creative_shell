from django.db import models


# Create your models here.
class CulturalHeritage(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    year_whs = models.IntegerField(default=2024, null=True)
    year_endangered = models.IntegerField(default=2024, null=True)
    # description = models.TextField()
    # source_link = models.URLField()
    # image = models.ImageField(upload_to='cultural_images/')
    # created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'cultural_heritage'

    def __str__(self):
        return self.name
