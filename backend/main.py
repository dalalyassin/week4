from fastapi import FastAPI
from routers import health, llm
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
app = FastAPI(
    title="LLM API",
    description="API for interacting with OpenAI LLM",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(llm.router)
