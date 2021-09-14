from unittest.mock import Mock
from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionModelAdminTest(TestCase):
	def setUp(self):
		Subscription.objects.create(name='Henrique Bastos', cpf='12345678901',
			                        email='henrique@bastos.net', phone='21-99618-6180')
		self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)

	def test_has_action(self):
		"""Action mark_as_paid should be installed."""
		self.assertIn('mark_as_paid', self.model_admin.actions)

	def test_mark_all(self):
		"""It should mark all selected subscriptions as paid."""
		queryset = Subscription.objects.all()

		mock = Mock()
		old_message_user = SubscriptionModelAdmin.message_user
		SubscriptionModelAdmin.message_user = mock

		self.model_admin.mark_as_paid(None, queryset)

		self.assertEqual(1, Subscription.objects.filter(paid=True).count())

		SubscriptionModelAdmin.message_user = old_message_user

	def test_message(self):
		"""It should send a message to the user."""
		queryset = Subscription.objects.all()

		mock = Mock()
		old_message_user = SubscriptionModelAdmin.message_user
		SubscriptionModelAdmin.message_user = mock

		self.model_admin.mark_as_paid(None, queryset)

		mock.assert_called_once_with(None, '1 inscrição foi marcada como paga.')

		SubscriptionModelAdmin.message_user = old_message_user
