from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
	def setUp(self):
		data = dict(name='Henrique Bastos', cpf='12345678901',
				    email='henrique@bastos.net', phone='21-99618-6180')
		self.client.post('/inscricao/', data)
		self.email = mail.outbox[0]

	def test_subscription_email_subject(self):
		expect = 'Confirmação de inscrição'

		self.assertEqual(expect, self.email.subject)

	def test_subscription_email_from(self):
		expect = 'contato@eventex.com.br'

		self.assertEqual(expect, self.email.from_email)

	def test_subscription_email_to(self):
		expect = ['contato@eventex.com.br', 'henrique@bastos.net']

		self.assertEqual(expect, self.email.to)

	def test_subscription_email_body(self):

		self.assertIn('Henrique Bastos', self.email.body)
		self.assertIn('12345678901', self.email.body)
		self.assertIn('henrique@bastos.net', self.email.body)
		self.assertIn('21-99618-6180', self.email.body)
