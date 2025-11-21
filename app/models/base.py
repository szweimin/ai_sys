from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    """基础响应模型"""

    success: bool = True
    message: str = "Operation completed successfully"
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())


class PaginatedResponse(BaseResponse):
    """分页响应模型"""

    page: int = 1
    page_size: int = 10
    total: int = 0
    total_pages: int = 0


class ErrorResponse(BaseResponse):
    """错误响应模型"""

    success: bool = False
    error_code: str = "UNKNOWN_ERROR"
    details: Optional[dict] = None
