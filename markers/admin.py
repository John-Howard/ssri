"""Markers admin."""

from django.contrib.gis import admin
from markers.models import Marker


class CustomGeoModelAdmin(admin.GISModelAdmin):
    gis_widget_kwargs = {
        "attrs": {
            "default_zoom": 9,
            "default_lon": -0.2,
            "default_lat": 51.9,
            "map_width": 700,
            "map_height": 500,
        },
    }


@admin.register(Marker)
class MarkerAdmin(CustomGeoModelAdmin):
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
