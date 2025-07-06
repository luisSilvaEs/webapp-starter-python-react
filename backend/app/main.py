from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas.health import HealthResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", response_model=HealthResponse)
async def health():
    return {"status": "ok"}
