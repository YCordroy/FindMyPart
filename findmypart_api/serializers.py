async def serialize_part(part):
    return {
        "mark": {
            "id": part['mark_id'],
            "name": part['mark_name'],
            "producer_country_name": part['producer_country_name'],
        },
        "model": {
            "id": part['model_id'],
            "name": part['model_name'],
        },
        "name": part['name'],
        "json_data": part['json_data'],
        "price": float(part['price']),
    }


async def serialize_search_part(parts, count, summ):
    serialized_parts: list[dict] = [await serialize_part(part) for part in parts]
    return {
        "response": serialized_parts,
        "count": count,
        "summ": float(summ),
    }
