from django.test import TestCase
from django.shortcuts import resolve_url as r


class TalkListGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('talk_list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

