from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestHealthEndpoints:
    """健康检查端点测试"""

    def test_health_status_is_ok(self) -> None:
        """测试 /api/v1/health 端点返回 status: ok"""
        response = client.get("/api/v1/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "message" in data
        assert "timestamp" in data

    def test_detailed_health_check(self) -> None:
        """测试 /api/v1/health/detailed 端点"""
        response = client.get("/api/v1/health/detailed")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "message" in data
        assert data["message"] == "All services are running normally"
        assert "timestamp" in data

    def test_sync_health_endpoint(self) -> None:
        """测试同步健康检查端点"""
        response = client.get("/api/v1/health/sync")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["message"] == "Sync health check successful"


def test_root_endpoint() -> None:
    """测试根端点"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data


def test_api_info() -> None:
    """测试 API 信息端点"""
    response = client.get("/info")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "AI System API"
    assert data["status"] == "running"
