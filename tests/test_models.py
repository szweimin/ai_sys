import pytest
from datetime import datetime
from typing import Any, Dict
from app.models.schemas.user import UserCreate, UserResponse, UserRole
from app.models.schemas.ai import ChatRequest, Message, ChatRole
from app.models.schemas.rag import RAGQueryRequest, RAGQueryResponse


class TestUserModels:
    """用户模型测试"""

    def test_user_create_valid(self) -> None:
        """测试有效的用户创建模型"""
        user_data = {"email": "test@example.com", "username": "testuser", "password": "securepassword123"}
        user = UserCreate(**user_data)
        assert user.email == "test@example.com"
        assert user.username == "testuser"

    def test_user_create_invalid_email(self) -> None:
        """测试无效邮箱的用户创建模型"""
        with pytest.raises(ValueError):
            UserCreate(email="invalid-email", username="testuser", full_name="david", password="securepassword123")

    def test_user_response_model(self) -> None:
        """测试用户响应模型"""
        user_data: Dict[str, Any] = {
            "id": "user123",
            "email": "test@example.com",
            "username": "testuser",
            "full_name": "Test User",
            "role": UserRole.USER,
            "is_active": True,
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        }
        user = UserResponse(**user_data)
        assert user.id == "user123"
        assert user.role == UserRole.USER


class TestAIModels:
    """AI 模型测试"""

    def test_chat_request_valid(self) -> None:
        """测试有效的聊天请求模型"""
        messages = [Message(role=ChatRole.USER, content="Hello")]
        chat_request = ChatRequest(
            messages=messages, model="gpt-3.5-turbo", temperature=0.7, max_tokens=100, stream=False
        )
        assert len(chat_request.messages) == 1
        assert chat_request.temperature == 0.7

    def test_rag_query_request_valid(self) -> None:
        """测试有效的 RAG 查询请求模型"""
        rag_request = RAGQueryRequest(
            query="What is AI?", top_k=5, temperature=0.7, max_tokens=100, include_contexts=True
        )
        assert rag_request.query == "What is AI?"
        assert rag_request.top_k == 5
        assert rag_request.temperature == 0.7


class TestRAGModels:
    """RAG 模型测试"""

    def test_rag_query_response_valid(self) -> None:
        """测试有效的 RAG 查询响应模型"""

        response_data: Dict[str, Any] = {
            "query": "What is AI?",
            "answer": "AI is artificial intelligence...",
            "contexts": [],
            "context_count": 0,
            "model_used": "gpt-3.5-turbo",
            "processing_time": 1.5,
            "status": "success",
        }
        response = RAGQueryResponse(**response_data)
        assert response.query == "What is AI?"
        assert response.status == "success"
