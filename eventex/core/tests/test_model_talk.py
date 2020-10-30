from django.test import TestCase
from eventex.core.models import Talk


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title='Título da Palestra',
            start='10:00',
            description='Descrição da palestra.'
        )

    def test_create(self):
        self.assertTrue(Talk.objects.exists())