from django.test import TestCase


class TalkListGet(TestCase):
    def test_get(self):
        resp = self.client.get('/palestras/')
        self.assertEqual(200, resp.status_code)