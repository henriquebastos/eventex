from django.test import TestCase


class SubscribeTest(TestCase):
	def test_get(self):
		"""Get /inscricao/ must return status code 200"""
		response = self.client.get('/inscricao/')
		self.assertEqual(200, response.status_code)
		