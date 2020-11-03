from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='https://hbn.link/hb-pic'
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='henrique@bastos.net'
        )

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='21-996186180'
        )

        self.assertTrue(Contact.objects.exists())

    def test_choice(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='A',
            value='B'
        )

        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='henrique@bastos.net'
        )

        self.assertEqual('henrique@bastos.net', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
           name='Henrique Bastos',
           slug='henrique-bastos',
           photo='http://hbn.link/hb-pic'
        )

        s.contact_set.create(kind=Contact.EMAIL, value='henrique@bastos.net')
        s.contact_set.create(kind=Contact.PHONE, value='21-996186180')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['henrique@bastos.net']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['21-996186180']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)