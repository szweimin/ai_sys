from fastapi import APIRouter
from app.services.health_service import HealthService

router = APIRouter()
health_service = HealthService()


@router.get("")
async def health_check() -> dict:
    """
    健康检查端点
    """
    return await health_service.check_health()


@router.get("/detailed")
async def detailed_health_check() -> dict:
    """
    详细健康检查端点
    """
    return await health_service.detailed_health_check()


@router.get("/sync")
def sync_health_check() -> dict:
    """
    同步健康检查端点（用于测试）
    """
    return {"status": "ok", "message": "Sync health check successful"}
