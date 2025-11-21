from fastapi import FastAPI
from app.api.v1.router import router as api_router

# 创建 FastAPI 应用实例
app = FastAPI(
    title="AI System API",
    description="AI Infrastructure System API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# 包含 API 路由
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root() -> dict:
    """
    根端点
    """
    return {"message": "Welcome to AI System API", "version": "1.0.0", "docs": "/docs", "health": "/api/v1/health"}


@app.get("/info")
async def api_info() -> dict:
    """
    API 信息端点
    """
    return {"name": "AI System API", "status": "running", "version": "1.0.0"}
