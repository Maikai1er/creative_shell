# Generated by Django 5.0.4 on 2024-07-25 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parseddata',
            name='image_path',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='parseddata',
            name='reason',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='parseddata',
            name='year',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
