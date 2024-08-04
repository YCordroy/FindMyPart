import json

from django.http import JsonResponse
from django.core.paginator import Paginator
from django.conf import settings
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt

from .filters import search_parts_filter
from .models import Mark, Model, Part
from .serializers import serialize_search_part


@require_GET
def get_mark_list(request):
    marks = Mark.objects.filter(is_visible=True)
    data = [
        {
            'mark_id': mark.id,
            'name': mark.name,
            'producer_country_name': mark.producer_country_name
        } for mark in marks
    ]
    return JsonResponse(data, safe=False)


@require_GET
def get_model_list(request):
    models = Model.objects.filter(is_visible=True)
    data = [
        {
            'model_id': model.id,
            'name': model.name,
        } for model in models
    ]
    return JsonResponse(data, safe=False)


@require_POST
@csrf_exempt
def search_parts(request):
    """
        Фильтрация запчастей
        Параметры:mark_name, mark_list, params,
        page, price_gte, price_lte, part_name
    """
    data = json.loads(request.body.decode('utf-8'))
    query = search_parts_filter(data)

    queryset = (
        Part
        .objects
        .select_related('mark', 'model')
        .filter(query, is_visible=True)
        .order_by('id')
    )

    paginator = Paginator(queryset, settings.PAGINATE_NUMBER)
    page = data['page'] if data.get('page') else 1
    current_page = paginator.get_page(page)

    data = serialize_search_part(queryset, current_page)

    return JsonResponse(data, safe=False)
