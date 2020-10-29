from django.test import TestCase


class SpeakerDetailGet(TestCase):
    def test_get(self):
        """GET should return status 200"""
        response = self.client.get('/palestrantes/grace-hopper')
        self.assertEqual(200, response.status_code)
