from findmypart_api.database import app
from search.routers import router


app.include_router(router)
