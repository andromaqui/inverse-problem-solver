from fastapi import FastAPI
from source.api import router

app = FastAPI()
app.include_router(router)
