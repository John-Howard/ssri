# Generated by Django 3.2.6 on 2021-09-13 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='marker',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
    ]