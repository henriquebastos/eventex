from django.test import TestCase


class SubscribeTest(TestCase):
	def setUp(self):
		self.resp = self.client.get('/inscricao/')

	def test_get(self):
		"""Get /inscricao/ must return status code 200"""
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		"""Must use subscriptions/subscription_form.html"""
		self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

	def test_html(self):
		"""Html must contain input tags"""
		self.assertContains(self.resp, '<form')
		self.assertContains(self.resp, '<input', 5)
		self.assertContains(self.resp, 'type="text"', 3)
		self.assertContains(self.resp, 'type="email"')
		self.assertContains(self.resp, 'type="submit"')
