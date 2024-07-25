from django.core.exceptions import ValidationError
from django.db import models


class CulturalHeritage(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    year = models.CharField(max_length=255, blank=True, default='')
    reason = models.TextField(blank=True, default='')
    image_path = models.CharField(max_length=255, blank=True, default='')

    def clean(self):
        if not isinstance(self.year, str):
            raise ValidationError({'year': 'Year must be a string'})

    class Meta:
        db_table = 'cultural_heritage'

    def __str__(self):
        return self.name


class ContactData(models.Model):
    name = models.CharField(max_length=255)
    contacts = models.TextField()
    about = models.TextField(blank=True, default='')

    class Meta:
        db_table = 'contact_data'

    def __str__(self):
        return self.name
    #   This is here because I'm lazy. This is a model for contact info from partnership form
