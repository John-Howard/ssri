"""Organisations models."""

from django.contrib.gis.db import models


class Organisation(models.Model):
    """An organisation with name and location."""

    uprn = models.PositiveBigIntegerField("UPRN", default=0)
    name = models.CharField(max_length=255)
    building_name_or_number = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city_or_town = models.CharField(max_length=255)
    postcode = models.CharField(max_length=8)
    location = models.PointField()

    def __str__(self):
        """Return string representation."""
        return self.name
