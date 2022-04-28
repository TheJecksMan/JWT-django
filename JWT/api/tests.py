from django.test import TestCase
import base64


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AccountTests(APITestCase):

    def test_login_account(self):
        """
        Тестирование  входа в систему
        """
        username = 'marvin'
        password = '12345'

        url = reverse('login')
        auth_headers = {'HTTP_AUTHORIZATION': 'Basic ' + f'{username}:{password}', }
        response = self.client.post(url,  **auth_headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
