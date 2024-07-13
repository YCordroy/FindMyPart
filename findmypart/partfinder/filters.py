import json

from django.db.models import Q


def search_parts_filter(data):
    """Формирование подзапроса для фильтра запчастей"""
    query = Q()
    # Добавление фильтров из запроса
    if data.get('mark_name'):
        query &= Q(mark__name__icontains=data['mark_name'])
    if data.get('part_name'):
        query &= Q(name__icontains=data['part_name'])
    if data.get('price_gte'):
        query &= Q(price__gte=data['price_gte'])
    if data.get('price_lte'):
        query &= Q(price__lte=data['price_lte'])
    if data.get('params'):
        # Обработка вложенных параметров
        request_params = data['params']
        params_encode = {
            f'json_data__{param}__icontains': value
            for param, value in request_params.items()
        }
        query &= Q(**params_encode)
    if data.get('mark_list'):
        mark_list = json.loads(data['mark_list'])
        query &= Q(mark__id__in=mark_list)

    return query
