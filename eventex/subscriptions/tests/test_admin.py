from unittest.mock import Mock
from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionModelAdminTest(TestCase):
	def test_has_action(self):
		"""Action mark_as_paid should be installed."""
		model_admin = SubscriptionModelAdmin(Subscription, admin.site)
		self.assertIn('mark_as_paid', model_admin.actions)

	def test_mark_all(self):
		"""It should mark all selected subscriptions as paid."""
		Subscription.objects.create(name='Henrique Bastos', cpf='12345678901',
			                        email='henrique@bastos.net', phone='21-99618-6180')
		model_admin = SubscriptionModelAdmin(Subscription, admin.site)

		queryset = Subscription.objects.all()

		mock = Mock()
		old_message_user = SubscriptionModelAdmin.message_user
		SubscriptionModelAdmin.message_user = mock

		model_admin.mark_as_paid(None, queryset)

		self.assertEqual(1, Subscription.objects.filter(paid=True).count())

		SubscriptionModelAdmin.message_user = old_message_user

	def test_message(self):
		"""It should send a message to the user."""
		Subscription.objects.create(name='Henrique Bastos', cpf='12345678901',
			                        email='henrique@bastos.net', phone='21-99618-6180')
		model_admin = SubscriptionModelAdmin(Subscription, admin.site)

		queryset = Subscription.objects.all()

		mock = Mock()
		old_message_user = SubscriptionModelAdmin.message_user
		SubscriptionModelAdmin.message_user = mock

		model_admin.mark_as_paid(None, queryset)

		mock.assert_called_once_with(None, '1 inscrição foi marcada como paga.')

		SubscriptionModelAdmin.message_user = old_message_user
