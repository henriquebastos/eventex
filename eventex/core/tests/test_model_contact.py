from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='https://hbn.link/hb-pic'
        )

        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='E',
            value='henrique@bastos.net'
        )

        self.assertTrue(Contact.objects.exists())
