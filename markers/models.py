"""Markers models."""

from django.contrib.gis.db import models


class Marker(models.Model):
    """A marker with name and location."""

    name = models.CharField(max_length=255)
    location = models.PointField()
    description = models.CharField(max_length=255, default='')
    linked_document = models.URLField(max_length=200, default='')

    def __str__(self):
        """Return string representation."""
        return self.name
