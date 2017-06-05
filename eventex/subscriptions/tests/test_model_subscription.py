from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
	def test_create(self):
		obj = Subscription(
			name='Henrique Bastos',
			cpf='12345678901',
			email='henrique@bastos.net',
			phone='21-99618-6180'
		)
		obj.save()
		self.assertTrue(Subscription.objects.exists())
