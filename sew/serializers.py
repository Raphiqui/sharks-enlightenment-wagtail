from rest_framework import serializers

from home.models import SharkPage


class SharkSerializer(serializers.ModelSerializer):
    """
    Global serializer for Shark model.
    Almost all the data are interesting, basically aims to be displayed into shark page.
    """

    class Meta:
        model = SharkPage
        fields = [
            "id",
            "title",
            "scientific_name",
            "description",
            "image",
            "iucn_status",
            "distribution",
        ]
