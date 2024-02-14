import logging
import pytest
from django.test import TestCase
from model_bakery import baker

from home.models import SharkPage

logger = logging.getLogger(__name__)


class TestSerializer(TestCase):
    """ """

    @pytest.mark.django_db
    def setUp(self):
        """
        pytest allows to create a fake db to populate it with some mockedup data
        """

        # self.shark = baker.make(SharkPage)
        print("fooo")

    def test_serializer_is_valid(self):
        value = True
        assert bool(value) is True
