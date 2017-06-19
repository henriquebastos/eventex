from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
	def setUp(self):
		self.form = SubscriptionForm()

	def test_form_has_fields(self):
		"""Form must have 4 fields"""
		expected = ['name', 'cpf', 'email', 'phone']
		self.assertSequenceEqual(expected, list(self.form.fields))

	def test_cpf_is_digit(self):
		"""CPF must only accept digits."""
		data = dict(name='Henrique Bastos', cpf='ABCD5678901',
			        email='henrique@bastos.net', phone='21-996186180')
		form = SubscriptionForm(data)
		form.is_valid()

		self.assertListEqual(['cpf'], list(form.errors))

	def test_cpf_has_11_digits(self):
		"""CPF must have 11 digits"""
		data = dict(name='Henrique Bastos', cpf='1234',
			        email='henrique@bastos.net', phone='21-996186180')
		form = SubscriptionForm(data)
		form.is_valid()

		self.assertListEqual(['cpf'], list(form.errors))

