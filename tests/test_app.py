from app.main import app


def test_app_starts():
    assert app.title == "AI Infra Base API"
    assert app.version == "1.0.0"
