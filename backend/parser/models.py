from django.db import models


class ParsedData(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    year_endangered = models.IntegerField(default=2024, null=True)
    reason = models.TextField(null=True, blank=True)
    image_path = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'parsed_data'

    def __str__(self):
        return self.name
