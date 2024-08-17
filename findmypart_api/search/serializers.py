import json

from .schemas import (
    MarkResponse,
    ModelResponse,
    PartResponse,
    SearchResponse
)


async def serialize_part(part):
    mark = MarkResponse(
        mark_id=part['mark_id'],
        name=part['mark_name'],
        producer_country_name=part['producer_country_name']
    )
    model = ModelResponse(
        model_id=part['model_id'],
        name=part['model_name']
    )
    part = PartResponse(
        mark=mark,
        model=model,
        name=part['name'],
        json_data=json.loads(part["json_data"]),
        price=float(part['price'])
    )
    return part


async def serialize_search_part(parts, count, summ):
    serialized_parts: list[PartResponse] = [
        await serialize_part(part) for part in parts
    ]
    search_response = SearchResponse(
        response=serialized_parts,
        count=count,
        summ=float(summ)
    )
    return search_response
