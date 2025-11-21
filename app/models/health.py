from pydantic import BaseModel


class HealthStatus(BaseModel):
    """健康检查响应模型"""

    status: str
    message: str = "Service is healthy"
    timestamp: str = ""

    class Config:
        schema_extra = {
            "example": {"status": "ok", "message": "Service is healthy", "timestamp": "2024-01-01T00:00:00Z"}
        }
