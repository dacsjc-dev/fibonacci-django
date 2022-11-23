#from rest_framework.test import APITestCase
from .test_setup import TestSetup

class TestViews(TestSetup):
    def test_cannot_request_fibonacci_with_no_data(self):
        response = self.client.post(self.fibonacci_url)
        self.assertEqual(response.status_code, 400)

    def test_happy_path_fibonacci_status_201(self):
        response = self.client.post(self.fibonacci_url, self.mock_data['request_body'], format="json")
        self.assertEqual(response.status_code, 201)