from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.process import router as process_router

app = FastAPI(title="Agentic AI App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(process_router)

@app.get("/")
def home():
    return {"message": "Agentic AI Backend Running"}