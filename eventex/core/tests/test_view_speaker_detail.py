from django.test import TestCase
from django.shortcuts import resolve_url as r


class SpeakerDetailGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('speaker_detail', slug='grace-hopper'))

    def test_get(self):
        """GET should return status 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        contents = [
            'Grace Hopper',
            'Programadora e almirante.',
            'http://hbn.link/hopper-pic',
            'http://hbn.link/hopper-site',
        ]

        for expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected)
