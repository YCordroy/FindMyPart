# FindMyPart

___

**Описание**:

Инструмент для поиска деталей и компонентов.<br>
Представляет собой две версии реализации Api эндпоинтов.<br>

Вополнен на:
* Djanjo
* FastApi

Используется база данных PostgeSQL и для проксирования запросов Nginx.
___

## Реализация Django

Написана без использывания DRF.<br>
Для ускорения работы, убраны все стандартные приложения.<br>
В данной версии реализованы три эндпоинта:

* `mark/` - Возвращает список всех марок.
* `model/` - Возвращает список моделей.
* `search/part/` - Поиск запчастей по заданному фильтру.
* `search/model/` - Поиск модели по фильтру `mark_name`.

В данной реализации все запросы идут через ORM.


Предусмотренно заполнение базы данныхь для тестов:

Заполнение базы данных марками и моделями.

```
python manage.py generate_mark_model
```

Заполнение базы данных запчастями, 10000 за один вызов.

```
python manage.py generate_parts
```

___

## Реализация FastApi

Реализован один эндпоинт:

* `search/part/` - Поиск запчастей по заданному фильтру.

Для запросов используется чистый SQL

___

## Фильтры для поиска:

* `mark_name` - Поиска по марке.
* `part_name` - Поиск по названию запчасти.
* `price_gte` - Нижняя граница цены поиска.
* `price_lte` - Верхняя граница цены поиска.
* `params:` - Дополнительные параметры.
    * `is_new_part` - Новая запчасть.
    * `color` - Цвет запчасти.
    * `count` - Колличество запчастей.
* `mark_list` - Поиск по нескольким маркам.
* `page` - Выбор страницы.
*

Примеры запроса:

```json
{
  "mark_name": "honda",
  "part_name": "бампер",
  "params": {
    "color": "чёрный"
  },
  "page": 1
}
```

```json
{
  "mark_list": [
    1,
    3
  ],
  "part_name": "бамп",
  "params": {
    "is_new_part": false,
    "color": "белый"
  },
  "price_gte": 2000,
  "price_lte": 5000
}
```

Ответ:

```json
{
  "response": [
    {
      "mark": {
        "id": 1,
        "name": "Honda",
        "producer_country_name": "Япония"
      },
      "model": {
        "id": 2,
        "name": "Accord"
      },
      "name": "Бампер передний",
      "json_data": {
        "is_new_part": true,
        "color": "черный",
        "count": 4
      },
      "price": 2300
    }
  ],
  "count": 1,
  "summ": 2300
}
```

___

## Запуск проекта (Используется Docker-compose).

Клонирование репозитория.

```bash
git clone https://github.com/YCordroy/FindMyPart.git
```

В настройках Django (`findmypart/findmypart/settings.py`):

Изменить:
* `ALLOWED_HOSTS = [127.0.0.1]` -> `ALLOWED_HOSTS = [Адрес сервера]`

Запустить docker-compose.
```
sudo docker-compose -p findmypart up -d --build
```

### Эндпоинты будут доступны по адресам:

Django.
```
'http://вашсервер/django/...'
```
FastApi.
```
'http://вашсервер/fastapi/...'
