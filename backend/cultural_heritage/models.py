from django.db import models


class CulturalHeritage(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    year = models.CharField(default='Default', null=True)
    reason = models.TextField(null=True, blank=True)
    image_path = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'cultural_heritage'

    def __str__(self):
        return self.name


class ContactData(models.Model):
    name = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)
    about = models.CharField(max_length=255)

    class Meta:
        db_table = 'contact_data'

    def __str__(self):
        return self.name
    #   This is here because I'm lazy. This is a model for contact info from partnership form
