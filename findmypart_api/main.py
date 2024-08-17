from fastapi import FastAPI
from search.routers import router

app = FastAPI()
app.include_router(router)
