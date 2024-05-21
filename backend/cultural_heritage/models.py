from django.db import models


class CulturalHeritage(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    year = models.CharField(default=2024, null=True)
    description = models.TextField(null=True)
    category = models.CharField(max_length=255, null=True)

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
