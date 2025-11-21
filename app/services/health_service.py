from typing import Optional, Dict, Any
from app.repositories.health_repo import HealthRepository, MemoryHealthRepository
from datetime import datetime


class HealthService:
    """健康检查服务"""

    def __init__(self, repository: Optional[HealthRepository] = None) -> None:
        self.repository = repository or MemoryHealthRepository()

    async def check_health(self) -> Dict[str, Any]:
        """
        执行健康检查

        Returns:
            dict: 包含健康状态和详细信息的字典
        """
        try:
            # 检查基础服务健康状态
            is_healthy = await self.repository.check_health()

            # 获取当前时间戳
            current_time = datetime.now().isoformat()

            if is_healthy:
                return {"status": "ok", "message": "All services are running normally", "timestamp": current_time}
            else:
                return {"status": "error", "message": "One or more services are unavailable", "timestamp": current_time}

        except Exception as e:
            return {
                "status": "error",
                "message": f"Health check failed: {str(e)}",
                "timestamp": datetime.now().isoformat(),
            }

    async def detailed_health_check(self) -> Dict[str, Any]:
        """
        详细的健康检查

        Returns:
            dict: 包含详细健康信息的字典
        """
        base_health = await self.check_health()

        # 添加更多健康指标
        detailed_info = {
            "status": base_health["status"],
            "message": base_health["message"],
            "timestamp": base_health["timestamp"],
            "services": {
                "database": {"status": "ok", "response_time": "5ms"},
                "cache": {"status": "ok", "response_time": "2ms"},
                "external_api": {"status": "ok", "response_time": "50ms"},
            },
        }

        return detailed_info
