from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
	def test_form_has_fields(self):
		"""Form must have 4 fields"""
		form = SubscriptionForm()
		expected = ['name', 'cpf', 'email', 'phone']
		self.assertSequenceEqual(expected, list(form.fields))

	def test_cpf_is_digit(self):
		"""CPF must only accept digits."""
		form = self.make_validated_form(cpf='ABCD5678901')
		self.assertListEqual(['cpf'], list(form.errors))

	def test_cpf_has_11_digits(self):
		"""CPF must have 11 digits"""
		form = self.make_validated_form(cpf='1234')
		self.assertListEqual(['cpf'], list(form.errors))

	def make_validated_form(self, **kwargs):
		valid = dict(name='Henrique Bastos', cpf='12345678901',
			         email='henrique@bastos.net', phone='21-996186180')
		data = dict(valid, **kwargs)
		form = SubscriptionForm(data)
		form.is_valid()
		return form
