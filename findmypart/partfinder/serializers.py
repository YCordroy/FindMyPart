from django.db.models import Sum


def serialize_part(part):
    return {
        "mark": {
            "id": part.mark.id,
            "name": part.mark.name,
            "producer_country_name": part.mark.producer_country_name,
        },
        "model": {
            "id": part.model.id,
            "name": part.model.name,
        },
        "name": part.name,
        "json_data": part.json_data,
        "price": float(part.price),
    }


def serialize_search_part(queryset, current_page):
    total_count = queryset.count()

    total_sum = queryset.aggregate(
        total_sum=Sum('price')
    )['total_sum'] or 0.0

    serialized_parts = [serialize_part(part) for part in current_page]
    return {
        "response": serialized_parts,
        "count": total_count,
        "summ": float(total_sum),
    }


def serialize_mark(mark):
    return {
        'mark_id': mark.id,
        'name': mark.name,
        'producer_country_name': mark.producer_country_name
    }


def serialize_model(model):
    return {
        'mark': {
            "id": model.mark.id,
            "name": model.mark.name,
            "producer_country_name": model.mark.producer_country_name,
        },
        'model': {
            'name': model.name,
            'model_id': model.id,
        }
    }
