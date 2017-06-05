from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionModelAdminTest(TestCase):
	def test_has_action(self):
		"""Action mark_as_paid should be installed."""
		model_admin = SubscriptionModelAdmin(Subscription, admin.site)
		self.assertIn('mark_as_paid', model_admin.actions)
