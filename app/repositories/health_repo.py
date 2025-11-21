from abc import ABC, abstractmethod


class HealthRepository(ABC):
    """健康检查仓库接口"""

    @abstractmethod
    async def check_health(self) -> bool:
        """检查服务健康状态"""
        pass


class MemoryHealthRepository(HealthRepository):
    """内存健康检查仓库实现"""

    async def check_health(self) -> bool:
        """简单的内存健康检查，总是返回 True"""
        # 这里可以添加更复杂的健康检查逻辑
        # 比如检查数据库连接、外部服务状态等
        return True
