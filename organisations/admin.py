"""Organisations admin."""

from django.contrib.gis import admin
from organisations.models import Organisation


@admin.register(Organisation)
class OrganisationAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    list_display = (
        "name",
        "building_name_or_number",
        "street",
        "city_or_town",
        "postcode",
        "uprn",
    )
