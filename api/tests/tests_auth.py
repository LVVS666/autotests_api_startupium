from api.page.base import ApiBase


def test_successful_login():
    '''Валидная авторизация'''
    page_auth = ApiBase(
        url='/api/login',
        headers={
            'Content-Type': 'application/json'
        },
        payload={
            "email": "LoVasya33@yandex.ru",
            "password": "Password1!"
        })
    response = page_auth.post()
    response_data = response.json()
    page_auth.assert_equal(response.status_code, 200, f"Статус код ответа не 200, вернулся {response.status_code}")
    page_auth.assert_in('token', response_data['data'], 'Токен не найден')
    page_auth.assert_in('refreshToken', response_data['data'], 'Рефреш токен не найден')


def test_unauthorized_login():
    '''Проверка отработки ошибки с неверными данными'''
    page_auth = ApiBase(
        url='/api/login',
        headers={
            'Content-Type': 'application/json'
        },
        payload={
            "email": "LoVasya33@yandex.ru",
            "password": "Not_valide"
        })
    response = page_auth.post()
    page_auth.assert_equal(response.status_code, 400, f"Статус код ответа не 401, вернулся {response.status_code}")
    response_data = response.json()
    page_auth.assert_in('message', response_data, 'Отсутствует сообщение об ошибке')


def test_user_not_found():
    '''Запрос авторизации на пользователя которого нет в базе'''
    page_auth = ApiBase(
        url='/api/login',
        headers={
            'Content-Type': 'application/json'
        },
        payload={
            "email": "not_user_in_datebase@mail.ru",
            "password": "password"
        })
    response = page_auth.post()
    page_auth.assert_equal(response.status_code, 400, f"Статус код ответа не 404, вернулся {response.status_code}")
    response_data = response.json()
    page_auth.assert_in('message', response_data, 'Отсутствует сообщение об ошибке')
