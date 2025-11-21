from pydantic import BaseModel, Field
from datetime import datetime
from typing import Dict, Any, Optional


class HealthStatus(BaseModel):
    """健康检查响应模型"""

    status: str = Field(..., description="服务状态: ok, warning, error")
    message: str = Field(..., description="状态消息")
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
    service: str = Field("ai-sys", description="服务名称")
    version: str = Field("1.0.0", description="服务版本")

    class Config:
        schema_extra = {
            "example": {
                "status": "ok",
                "message": "All services are running normally",
                "timestamp": "2024-01-01T00:00:00Z",
                "service": "ai-sys",
                "version": "1.0.0",
            }
        }


class DetailedHealthStatus(HealthStatus):
    """详细健康检查响应模型"""

    environment: str = Field("development", description="运行环境")
    uptime: Optional[float] = Field(None, description="运行时间（秒）")
    components: Dict[str, str] = Field(default_factory=dict, description="组件状态")
    metrics: Dict[str, Any] = Field(default_factory=dict, description="性能指标")

    class Config:
        schema_extra = {
            "example": {
                "status": "ok",
                "message": "All services are running normally",
                "timestamp": "2024-01-01T00:00:00Z",
                "service": "ai-sys",
                "version": "1.0.0",
                "environment": "development",
                "components": {"database": "healthy", "cache": "healthy", "api": "healthy"},
                "metrics": {"response_time": 0.15, "memory_usage": "45%"},
            }
        }
