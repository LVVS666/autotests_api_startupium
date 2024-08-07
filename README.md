# autotests_api_startupium

# Проект автоматизированного тестирования API для Startupium

Этот репозиторий содержит проект для автоматизированного тестирования API проекта Startupium. Мы используем `pytest` и `requests` для создания и выполнения тестов, а также `locust` для нагрузочного тестирования.

## Структура проекта

```
project-root/
├── api/
│   ├── page/
│   │   └── ... # Классы для тестов
│   ├── tests/
│   │   └── ... # Тестовые файлы
├── requirements.txt
├── locustfile.py
└── README.md
```

### api/page

В этой директории находятся классы, которые используются для тестирования. Эти классы включают в себя методы для различных API запросов.

### api/tests

Здесь находятся все тесты, которые используют классы из директории `page`.

## Установка

Для установки необходимых зависимостей выполните следующие команды:

```bash
pip install -r requirements.txt
```

## Запуск тестов

Для запуска тестов используйте `pytest`:

```bash
pytest
```

## Нагрузочное тестирование

Для выполнения нагрузочного тестирования используйте `locust`. Убедитесь, что у вас установлен `locust`:

```bash
pip install locust
```

Запуск `locust`:

```bash
locust -f locustfile.py
```

## Документация API

Для ознакомления с документацией API используйте [эту ссылку](https://docs.startupium.ru/sw/doc#/Auth/login).

## Главный сайт проекта

Больше информации о проекте вы можете найти на [главном сайте Startupium](https://startupium.ru/).
```
