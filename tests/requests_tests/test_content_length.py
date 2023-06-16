from django.urls import reverse
from django.test import TestCase, override_settings

@override_settings(ROOT_URLCONF='requests_tests.urls')
class TestContentLength(TestCase):
    def test_incorrect_content_length(self):
        url = reverse('index')
         # Simulate sending an incorrect Content-Length header
        response = self.client.post(url, data='1', content_type='text/plain', HTTP_ACCEPT='*/*', HTTP_CONTENT_LENGTH='22')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'')

        # Verify that the server is still responsive and not hanging
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'')

    def test_correct_content_length(self):
        url = reverse('index')
        # Simulate sending a correct Content-Length header
        response = self.client.post(url, data='1', content_type='text/plain', HTTP_ACCEPT='*/*', HTTP_CONTENT_LENGTH='1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'1')
