from django.test import TestCase


class HomeTest(TestCase):
	def test_get(self):
		"""GET / must return status code 200"""
		response = self.client.get('/')
		self.assertEqual(200, response.status_code)

	def test_template(self):
		"""Must use index.html"""
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'index.html')
