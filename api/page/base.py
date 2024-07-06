import requests

class ApiBase:
    '''Главный класс api'''
    base_url = 'https://startupium.ru'

    def __init__(self, url, headers=None, payload=None):
        self.url = self.base_url + url
        self.headers = headers
        self.payload = payload

    def post(self):
        '''Пост запрос'''
        return requests.post(self.url, json=self.payload, headers=self.headers)


    def assert_in(self, first, second, message):
        '''Проверка наличия элемента'''
        assert first in second, message

    def assert_equal(self, first, second, message):
        '''Сравнение элементов'''
        assert first == second, message