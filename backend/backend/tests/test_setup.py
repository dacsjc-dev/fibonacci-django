from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetup(APITestCase):

    def setUp(self):
        mock_data = {
            'test_id': 1,
            'request_body': {
                'n': 5
            }
        }

        self.fibonacci_url = reverse('fibonacci')
        self.fibonacci_details_url = reverse('fibonacci-details', kwargs={'id': mock_data['test_id']})
       
        self.mock_data = mock_data

        return super().setUp()

    def tearDown(self):
        return super().tearDown()