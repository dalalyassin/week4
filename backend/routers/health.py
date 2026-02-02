from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/")
def root():
    return {
        "message": "FastAPI is running",
        "docs": "/docs",
        "endpoint": "/ask"
    }

