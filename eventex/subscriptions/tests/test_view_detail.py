from django.test import TestCase


class SubscriptionDetailGet(TestCase):
	def setUp(self):
		self.resp = self.client.get('/inscricao/1/')

	def test_get(self):
		self.assertEqual(200, self.resp.status_code)
