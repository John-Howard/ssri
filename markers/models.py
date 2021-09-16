"""Markers models."""

from django.contrib.gis.db import models
from organisations.models import Organisation


class Marker(models.Model):
    """A marker with name and location."""

    name = models.CharField(max_length=255)
    reference_code = models.CharField(max_length=50, default='')
    classification_or_type = models.CharField(max_length=255, default='')
    is_published = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
    location = models.PointField()
    description = models.CharField(max_length=255, default='')
    linked_document = models.URLField(max_length=200, default='')
    uprn = models.PositiveBigIntegerField(default=0)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, default=1)

    def __str__(self):
        """Return string representation."""
        return self.name
