#from rest_framework.test import APITestCase
from .test_setup import TestSetup

class TestViews(TestSetup):
    def test_cannot_request_fibonacci_with_no_data(self):
        response = self.client.post(self.fibonacci_url)
        self.assertEqual(response.status_code, 400)

    def test_not_positive_integer_1(self):
        response = self.client.post(self.fibonacci_url, {"n": -1}, format="json")
        self.assertEqual(response.data, {'status': 'Invalid', 'message': 'n must be a positive integer'})
        self.assertEqual(response.status_code, 400)
    
    def test_not_positive_integer_2(self):
        response = self.client.post(self.fibonacci_url, {"n": "a"}, format="json")
        self.assertEqual(response.data, {'status': 'Invalid', 'message': 'n must be a positive integer'})
        self.assertEqual(response.status_code, 400)

    def test_happy_path_fibonacci_status_201(self):
        response = self.client.post(self.fibonacci_url, self.mock_data['request_body'], format="json")
        self.assertEqual(response.data, {'nth': '5', 'status': 'Success'})
        self.assertEqual(response.status_code, 201)

    # def test_happy_path_fibonacci_status_201_long(self):
    #     response = self.client.post(self.fibonacci_url, {"n": 10000}, format="json")
    #     self.assertEqual(response.data, {})
    #     self.assertEqual(response.status_code, 201)