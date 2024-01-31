from rest_framework import serializers

from home.models import SharkPage


class SharkPreviewSerializer(serializers.ModelSerializer):
    """
    Serializer for Shark model.
    Only the title and the scientific name are interesting, basically aims to be displayed into sharks page.
    """

    thumbnail = serializers.SerializerMethodField("get_thumbnail_rendition")

    def get_thumbnail_rendition(self, obj):
        """
        get_renditions methods allow to update an image without impacting the quality
        """

        return obj.image.get_renditions(
            "width-600", "height-400", "fill-300x186|jpegquality-60"
        )

    class Meta:
        model = SharkPage
        fields = ["title", "scientific_name", "thumbnail"]


class SharkSerializer(serializers.ModelSerializer):
    """
    Gloabl serializer for Shark model.
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
