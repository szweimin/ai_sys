from typing import Any
from fastapi import APIRouter
from app.models.health import HealthStatus, DetailedHealthStatus
from app.services.health_service import HealthService

router = APIRouter()


@router.get("", response_model=HealthStatus)
async def health_check() -> HealthStatus:
    """基础健康检查端点"""
    service = HealthService()
    health_data = await service.check_health()
    return HealthStatus(**health_data)


@router.get("/detailed", response_model=DetailedHealthStatus)
async def detailed_health_check() -> DetailedHealthStatus:
    """详细健康检查端点"""
    service = HealthService()
    health_data = await service.detailed_health_check()
    return DetailedHealthStatus(**health_data)


@router.get("/sync")
def sync_health_check() -> dict[Any, Any]:
    """同步健康检查端点（用于测试）"""
    return {"status": "ok", "message": "Sync health check successful"}
