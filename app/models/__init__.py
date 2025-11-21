from .base import BaseResponse, PaginatedResponse, ErrorResponse
from .health import HealthStatus, DetailedHealthStatus

# 用户相关模型
from .schemas.user import (
    UserBase,
    UserCreate,
    UserUpdate,
    UserInDB,
    UserResponse,
    UserLogin,
    Token,
    TokenData,
    UserRole,
)

# AI 相关模型
from .schemas.ai import (
    ModelProvider,
    ChatRole,
    Message,
    ChatRequest,
    ChatResponse,
    EmbeddingRequest,
    EmbeddingResponse,
    VectorSearchRequest,
    VectorSearchResult,
    VectorSearchResponse,
)

# RAG 相关模型
from .schemas.rag import (
    RAGQueryRequest,
    RAGQueryResponse,
    Document,
    DocumentCreate,
    DocumentUpdate,
    DocumentBatchResponse,
)

__all__ = [
    # 基础模型
    "BaseResponse",
    "PaginatedResponse",
    "ErrorResponse",
    # 健康检查
    "HealthStatus",
    "DetailedHealthStatus",
    # 用户模型
    "UserBase",
    "UserCreate",
    "UserUpdate",
    "UserInDB",
    "UserResponse",
    "UserLogin",
    "Token",
    "TokenData",
    "UserRole",
    # AI 模型
    "ModelProvider",
    "ChatRole",
    "Message",
    "ChatRequest",
    "ChatResponse",
    "EmbeddingRequest",
    "EmbeddingResponse",
    "VectorSearchRequest",
    "VectorSearchResult",
    "VectorSearchResponse",
    # RAG 模型
    "RAGQueryRequest",
    "RAGQueryResponse",
    "Document",
    "DocumentCreate",
    "DocumentUpdate",
    "DocumentBatchResponse",
]
