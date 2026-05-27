from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging

from .routes import aeroporti
from .logging_config import setup_logging


setup_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Aeroporti API started")
    yield

app = FastAPI(title="Aeroporti API", lifespan=lifespan)

app.include_router(aeroporti.router)

@app.get("/")
def root():
    logger.info("Health check called")
    return {"message": "Aeroporti API is running"}