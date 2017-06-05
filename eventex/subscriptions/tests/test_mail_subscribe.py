from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
	def setUp(self):
		data = dict(name='Henrique Bastos', cpf='12345678901',
				    email='henrique@bastos.net', phone='21-99618-6180')
		self.resp = self.client.post('/inscricao/', data)

	def test_subscription_email_subject(self):
		email = mail.outbox[0]
		expect = 'Confirmação de inscrição'

		self.assertEqual(expect, email.subject)

	def test_subscription_email_from(self):
		email = mail.outbox[0]
		expect = 'contato@eventex.com.br'

		self.assertEqual(expect, email.from_email)

	def test_subscription_email_to(self):
		email = mail.outbox[0]
		expect = ['contato@eventex.com.br', 'henrique@bastos.net']

		self.assertEqual(expect, email.to)

	def test_subscription_email_body(self):
		email = mail.outbox[0]

		self.assertIn('Henrique Bastos', email.body)
		self.assertIn('12345678901', email.body)
		self.assertIn('henrique@bastos.net', email.body)
		self.assertIn('21-99618-6180', email.body)
