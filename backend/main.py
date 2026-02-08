from fastapi import FastAPI
from routers import health
from app.routers import chat_api

app = FastAPI(
    title="LLM API",
    description="API for interacting with OpenAI LLM",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(chat_api.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
