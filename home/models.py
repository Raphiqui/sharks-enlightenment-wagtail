from django.db import models
from django.forms import model_to_dict

from wagtail.models import Page, Orderable
from wagtail import blocks
from wagtail.admin.panels import FieldPanel

from home.serializers import SharkPreviewSerializer


IUCN_STATUS = [
    ("LC", "Least Concern"),
    ("NT", "Near Threatened"),
    ("VU", "Vulnerable"),
    ("EN", "Endangered"),
    ("CR", "Critically Endangered"),
    ("EW", "Extinct in the Wild"),
    ("EX", "Extinct"),
]


class HomePage(Page):
    """
    This is the home page
    """

    subpage_types = ["home.AboutPage", "home.QuizzPage", "home.SharksPage"]

    class Meta:
        verbose_name = "Home page"


class AboutPage(Page):
    parrent_page_types = ["home.HomePage"]

    class Meta:
        verbose_name = "About page"


class QuizzPage(Page):
    parrent_page_types = ["home.HomePage"]

    class Meta:
        verbose_name = "Quizz page"


class SharksPage(Page):
    parent_page_types = ["home.HomePage"]

    subpage_types = ["home.SharkPage"]

    def get_context(self, request):
        context = super().get_context(request)
        shark_pages = SharkPage.objects.live().descendant_of(self)
        preview_data = [
            model_to_dict(
                shark_page, fields=["id", "title", "scientific_name", "image"]
            )
            for shark_page in shark_pages
        ]

        serializer = SharkPreviewSerializer(data=preview_data, many=True)

        if serializer.is_valid():
            context["sharks"] = serializer.data
        else:
            print(serializer.errors)
            context["sharks"] = []

        return context

    class Meta:
        verbose_name = "Sharks page"


class SharkPage(Page, Orderable):
    parent_page_types = ["home.SharksPage"]

    scientific_name = models.CharField(max_length=250, verbose_name="Scientific name")

    description = models.TextField(verbose_name="Description")

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Image",
    )

    iucn_status = models.CharField(
        max_length=100,
        choices=IUCN_STATUS,
        default=IUCN_STATUS[0][0],
        verbose_name="IUCN status",
    )
    distribution = models.TextField(verbose_name="Distribution")

    content_panels = Page.content_panels + [
        FieldPanel("scientific_name"),
        FieldPanel("description"),
        FieldPanel("image"),
        FieldPanel("iucn_status"),
        FieldPanel("distribution"),
    ]

    class Meta:
        verbose_name = "Shark page"
