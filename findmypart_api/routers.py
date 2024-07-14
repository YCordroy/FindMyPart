from fastapi import Depends, APIRouter

from database import get_db
from db_queries import search_part_sql
from serializers import serialize_search_part
from schemas import SearchResponse, SearchParams

router = APIRouter()


@router.post("/search/part/", response_model=SearchResponse)
def search_parts(data: SearchParams, conn=Depends(get_db)) -> SearchResponse:
    parts: tuple = search_part_sql(data, conn)
    data: dict = serialize_search_part(*parts)
    return data
