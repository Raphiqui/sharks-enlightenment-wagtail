import logging
import pytest

from home.models import SharkPage, SharksPage
from wagtail.models import Page, Locale
from wagtail.tests.utils import WagtailPageTestCase

from home.serializers import SharkPreviewSerializer

logger = logging.getLogger(__name__)


class TestSerializer(WagtailPageTestCase):

    @pytest.mark.django_db
    def setUp(self):
        """
        pytest allows to create a fake db to populate it with some mockedup data
        """

        locale = Locale.objects.create(language_code="en")

        Page.objects.create(title="Root", path="0001", depth=1, locale=locale)

        SharksPage.objects.create(
            title="Sharks", path="00010001", depth=2, locale=locale
        )

        SharkPage.objects.create(
            title="Great White Shark",
            description="The great white shark, also known as the great white, white shark or white pointer, is a species of large mackerel shark which can be found in the coastal surface waters of all the major oceans.",
            scientific_name="Carcharodon carcharias",
            distribution="The great white shark is mainly found in the coastal waters of all the major oceans.",
            path="000100010001",
            depth=3,
            locale=locale,
        )

        SharkPage.objects.create(
            title="Whale Shark",
            description="The whale shark is a slow-moving, filter-feeding carpet shark and the largest known extant fish species.",
            scientific_name="Rhincodon typus",
            distribution="The whale shark is found in open waters of the tropical oceans and is rarely found in water below 21 °C.",
            path="000100010002",
            depth=3,
            locale=locale,
        )

    def test_serializer_is_truthy(self):
        shark_page = SharkPage.objects.first()
        serializer = SharkPreviewSerializer(instance=shark_page)
        self.assertIsNotNone(serializer.data)

    def test_serializer_has_correct_fields(self):
        shark_page = SharkPage.objects.first()
        serializer = SharkPreviewSerializer(instance=shark_page)
        self.assertIn("id", serializer.data)
        self.assertIn("title", serializer.data)
        self.assertIn("scientific_name", serializer.data)
        self.assertIn("thumbnail", serializer.data)

    def test_serializer_thumbnail_may_be_empty(self):
        shark_page = SharkPage.objects.first()
        serializer = SharkPreviewSerializer(instance=shark_page)
        self.assertEquals(serializer.data["thumbnail"], "")

    def test_serializer_is_empty(self):
        serializer = SharkPreviewSerializer()
        self.assertEqual(
            serializer.data, {"id": None, "scientific_name": "", "title": ""}
        )

    def test_serializer_many_is_truthy(self):
        shark_pages = SharkPage.objects.all()
        serializer = SharkPreviewSerializer(instance=shark_pages, many=True)
        self.assertIsNotNone(serializer.data)

    def test_serializer_is_falsy(self):
        """
        Try to serialize an instance of a page which is not a SharksPage
        """

        serializer = SharkPreviewSerializer(instance=SharksPage.objects.first())
        with self.assertRaises(AttributeError):
            serializer.data
