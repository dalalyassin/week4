from fastapi import FastAPI
from routers import health, llm

app = FastAPI(
    title="LLM API",
    description="API for interacting with OpenAI LLM",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(llm.router)
