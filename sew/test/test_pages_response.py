import logging
import pytest

from home.models import SharksPage
from wagtail.models import Page, Locale
from wagtail.tests.utils import WagtailPageTestCase

logger = logging.getLogger(__name__)

from wagtail.models import Page, Locale

from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory


class TestSerializer(WagtailPageTestCase):

    @pytest.mark.django_db
    def setUp(self):
        """
        pytest allows to create a fake db to populate it with some mockedup data
        """

        locale = Locale.objects.create(language_code="en")

        Page.objects.create(title="Root", path="0001", depth=1, locale=locale)

        SharksPage.objects.create(
            title="Sharks", path="00010001", depth=2, locale=locale, slug="sharks"
        )

    def test_sharks_page_response(self):
        """
        Reverse from DRF needs some kind of <basename>-<action> to be able to resolve the URL
        """

        factory = APIRequestFactory()
        request = factory.get("/")
        url = reverse("Sharks-list", request=request)
        logger.info(f"Resolved URL for SharksViewSet: {url}")
        response = self.client.get(url)
        assert response.status_code == 200
