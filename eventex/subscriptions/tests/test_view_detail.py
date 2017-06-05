from django.test import TestCase


class SubscriptionDetailGet(TestCase):
	def setUp(self):
		self.resp = self.client.get('/inscricao/1/')

	def test_get(self):
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		self.assertTemplateUsed(self.resp,
								'subscriptions/subscription_detail.html')
