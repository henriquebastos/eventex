from django.test import TestCase
from eventex.core.models import Speaker

class SpeakerModelTest(TestCase):
    def test_create(self):
        speaker = Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            photo='http://hbn.link/hopper-pic',
            website='http://hbn.link/hopper-site',
            description='Programadora e almirante.',
        )

        self.assertTrue(Speaker.objects.exists())