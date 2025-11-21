from fastapi import FastAPI

app = FastAPI(title="AI Infra Base API", description="AI Infrastructure Base API", version="1.0.0")


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.get("/")
async def root():
    return {"message": "Welcome to AI Infra Base API"}
