from fastapi import APIRouter
from app.api.v1.endpoints import health

# 创建 API 路由器
router = APIRouter()

# 包含健康检查路由
router.include_router(health.router, prefix="/health", tags=["health"])
