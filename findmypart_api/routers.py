from fastapi import Depends, APIRouter

from database import get_db

router = APIRouter()


@router.get("/mark")
async def read_users(db=Depends(get_db)):
    cur = db.cursor()
    cur.execute("SELECT * FROM partfinder_mark")
    mark = cur.fetchall()
    return {"marks": mark}
