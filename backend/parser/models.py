from django.core.exceptions import ValidationError
from django.db import models


class ParsedData(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    year = models.CharField(max_length=255, default='Default', null=True)
    reason = models.TextField(null=True, blank=True)
    image_path = models.CharField(max_length=255, null=True, blank=True)

    def clean(self):
        if not isinstance(self.year, str):
            raise ValidationError({'year': 'Year must be a string'})

    class Meta:
        db_table = 'parsed_data'

    def __str__(self):
        return self.name
