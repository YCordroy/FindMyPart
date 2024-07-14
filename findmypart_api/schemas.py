from pydantic import BaseModel


class SearchParams(BaseModel):
    model_name: str | None = None
    mark_name: str | None = None
    part_name: str | None = None
    price_gte: float | None = None
    price_lte: float | None = None
    params: dict | None = None
    mark_list: list[int] | None = None
    page: int = 1


class PartResponse(BaseModel):
    mark: dict
    model: dict
    name: str
    json_data: dict
    price: float


class SearchResponse(BaseModel):
    response: list[PartResponse]
    count: int
    summ: float
