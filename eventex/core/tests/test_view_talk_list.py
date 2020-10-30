from django.test import TestCase
from django.shortcuts import resolve_url as r


class TalkListGet(TestCase):
    def test_get(self):
        resp = self.client.get(r('talk_list'))
        self.assertEqual(200, resp.status_code)