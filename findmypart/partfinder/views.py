from django.http import JsonResponse

from .models import Mark, Model


def get_mark_list(request):
    marks = Mark.objects.filter(is_visible=True)
    data = [
        {
            'mark_id': mark.id,
            'name': mark.name
        } for mark in marks
    ]
    return JsonResponse(data, safe=False)


def get_model_list(request):
    models = Model.objects.filter(is_visible=True)
    data = [
        {
            'model_id': model.id,
            'name': model.name,
            'mark': model.mark.name
        } for model in models
    ]
    return JsonResponse(data, safe=False)


# def search_parts(request):
#     mark_name = None,
#     mark_list = None,
#     params = None,
#     page = None,
#     price_gte = None,
#     price_lte = None,
#     part_name = None

