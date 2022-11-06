"""Markers admin."""

from django.contrib.gis import admin
from markers.models import Marker
from leaflet.admin import LeafletGeoAdmin


@admin.register(Marker)
class MarkerAdmin(LeafletGeoAdmin):
    pass
    """Marker admin."""

    list_display = (
        "name",
        "is_published",
        "reference_code",
        "location",
        "description",
        "linked_document",
        "classification_or_type",
        "created_at",
        "last_updated",
    )
