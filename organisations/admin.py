"""Organisations admin."""

from django.contrib.gis import admin
from organisations.models import Organisation
from leaflet.admin import LeafletGeoAdmin


@admin.register(Organisation)
class OrganisationAdmin(LeafletGeoAdmin):
    """Marker admin."""

    list_display = (
        "name",
        "building_name_or_number",
        "street",
        "city_or_town",
        "postcode",
        "uprn",
    )
