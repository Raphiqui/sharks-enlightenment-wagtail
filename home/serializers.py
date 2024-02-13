from rest_framework import serializers


class SharkPreviewSerializer(serializers.Serializer):
    """
    Data which aims to be displayed into sharks page
    """

    id = serializers.IntegerField()
    title = serializers.CharField()
    scientific_name = serializers.CharField()
    thumbnail = serializers.SerializerMethodField()

    def get_thumbnail(self, obj):
        """
        `get_rendition` allows to perfom image manipulation over images
        Also very useful to reduce the weight of the images, for instance a full image size weighting 330kb
        can be reduced to 30kb just by resizing it using `get_rendition` method, as so, page loads faster
        """
        if not obj.image:
            return ""

        rendition = obj.image.get_rendition("max-1000x500")
        return rendition.url
