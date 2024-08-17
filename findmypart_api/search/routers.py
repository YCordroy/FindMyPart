from fastapi import Depends, APIRouter

from .db_queries import search_part_sql
from findmypart_api.database import db
from .serializers import serialize_search_part
from .schemas import SearchResponse, SearchParams

router = APIRouter()


@router.post("/search/part/", response_model=SearchResponse)
async def search_parts(data: SearchParams, conn=Depends(db)) -> SearchResponse:
    parts: tuple = await search_part_sql(data, conn)
    data: dict = await serialize_search_part(*parts)
    return data
