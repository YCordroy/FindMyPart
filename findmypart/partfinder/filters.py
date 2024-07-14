from django.db.models import Q


def search_parts_filter(data):
    """Формирование подзапроса для фильтра запчастей"""
    query = Q()

    # Добавление фильтров из запроса
    filter_map = {
        'model_name': 'model__name__icontains',
        'mark_name': 'mark__name__icontains',
        'part_name': 'name__icontains',
        'price_gte': 'price__gte',
        'price_lte': 'price__lte'
    }
    params_filter = {
        filter_map[key]: value
        for key, value in data.items()
        if key in filter_map
    }
    query &= Q(**params_filter)

    # Обработка вложенных параметров
    if data.get('params'):
        request_params = data['params']
        params_encode = {
            f'json_data__{param}__icontains': value
            for param, value in request_params.items()
        }
        query &= Q(**params_encode)

    # Обработка нескольких марок
    if data.get('mark_list'):
        mark_list = data['mark_list']
        query &= Q(mark__id__in=mark_list)

    return query
