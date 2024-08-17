from pydantic import BaseModel, BaseConfig


class SearchParams(BaseModel):
    class Config(BaseConfig):
        protected_namespaces = ()

    model_name: str | None = None
    mark_name: str | None = None
    part_name: str | None = None
    price_gte: float | None = None
    price_lte: float | None = None
    params: dict | None = None
    mark_list: list[int] | None = None
    page: int = 1


class MarkResponse(BaseModel):
    mark_id: int
    name: str
    producer_country_name: str


class ModelResponse(BaseModel):
    model_id: int
    name: str


class PartResponse(BaseModel):
    mark: MarkResponse
    model: ModelResponse
    name: str
    json_data: dict
    price: float


class SearchResponse(BaseModel):
    response: list[PartResponse]
    count: int
    summ: float
