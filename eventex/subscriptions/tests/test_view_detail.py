from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
	def setUp(self):
		self.resp = self.client.get('/inscricao/1/')

	def test_get(self):
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		self.assertTemplateUsed(self.resp,
								'subscriptions/subscription_detail.html')

	def test_context(self):
		subscription = self.resp.context['subscription']
		self.assertIsInstance(subscription, Subscription)

	def test_html(self):
		contents = ('Henrique Bastos', '12345678901',
				    'henrique@bastos.net', '21-99618-6180')

		with self.subTest():
			for expected in contents:
				self.assertContains(self.resp, expected)
