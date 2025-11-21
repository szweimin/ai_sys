from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_app_starts() -> None:
    """测试应用能够正常启动"""
    assert app.title == "AI System API"
    assert app.description == "AI Infrastructure System API"
    assert app.version == "1.0.0"

    # 测试路由是否存在（使用 getattr 来避免对 BaseRoute 的未声明属性访问）
    routes = [getattr(route, "path", None) for route in app.routes]
    assert "/" in routes
    assert "/info" in routes

    # 测试 OpenAPI 文档端点
    assert "/docs" in routes
    assert "/redoc" in routes
