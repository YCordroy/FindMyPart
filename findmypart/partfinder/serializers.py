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
    total_sum = sum(part.price for part in queryset)
    serialized_parts = [serialize_part(part) for part in current_page]
    return {
        "response": serialized_parts,
        "count": total_count,
        "summ": float(total_sum),
    }
