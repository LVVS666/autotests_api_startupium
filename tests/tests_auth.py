import requests
from unittest import TestCase

class TestLoginEndpoint(TestCase):
    base_url = 'https://startupium.ru'

    def test_successful_login(self):
        url = f'{self.base_url}/api/login'
        headers = {'Content-Type': 'application/json'}
        payload = {
            "email": "LoVasya33@yandex.ru",
            "password": "Password1!"
        }
        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()
        self.assertEqual(response.status_code, 200, f"Статус код ответа не 200, вернулся {response.status_code}")
        self.assertIn('token', response_data['data'])
        self.assertIn('refreshToken', response_data['data'])

    def test_unauthorized_login(self):
        url = f'{self.base_url}/api/login'
        headers = {'Content-Type': 'application/json'}
        payload = {
            "email": "user_not_exiвst@mail.ru",
            "password": "InvalidPassword123"
        }
        response = requests.post(url, json=payload, headers=headers)
        self.assertEqual(response.status_code, 401, f"Статус код ответа не 401, вернулся {response.status_code}")
        response_data = response.json()
        self.assertIn('message', response_data)

    def test_user_not_found(self):
        url = f'{self.base_url}/api/login'
        headers = {'Content-Type': 'application/json'}
        payload = {
            "email": "non_existing_user@mail.ru",
            "password": "AnyPassword123"
        }
        response = requests.post(url, json=payload, headers=headers)
        self.assertEqual(response.status_code, 404, f"Статус код ответа не 404, вернулся {response.status_code}")
        response_data = response.json()
        self.assertIn('message', response_data)

