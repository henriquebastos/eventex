from django.test import TestCase


class SubscriptionDetailGet(TestCase):
	def test_get(self):
		resp = self.client.get('/inscricao/1/')
		self.assertEqual(200, resp.status_code)
