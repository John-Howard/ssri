"""Organisations admin."""

from django.contrib.gis import admin

from organisations.models import Organisation


@admin.register(Organisation)
class OrganisationAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    list_display = ("uprn", "name", "building_name_or_number", "city_or_town", "street", "postcode")
