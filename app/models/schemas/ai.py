from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class ModelProvider(str, Enum):
    """模型提供商枚举"""

    OPENAI = "openai"
    OLLAMA = "ollama"
    ANTHROPIC = "anthropic"
    LOCAL = "local"


class ChatRole(str, Enum):
    """聊天角色枚举"""

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class Message(BaseModel):
    """消息模型"""

    role: ChatRole = Field(..., description="消息角色")
    content: str = Field(..., description="消息内容")
    timestamp: datetime = Field(default_factory=datetime.now)


class ChatRequest(BaseModel):
    """聊天请求模型"""

    messages: List[Message] = Field(..., description="消息列表")
    model: str = Field("gpt-3.5-turbo", description="模型名称")
    temperature: float = Field(0.7, ge=0.0, le=2.0, description="温度参数")
    max_tokens: Optional[int] = Field(None, description="最大token数")
    stream: bool = Field(False, description="是否流式输出")

    class Config:
        schema_extra = {
            "example": {
                "messages": [{"role": "user", "content": "Hello, how are you?"}],
                "model": "gpt-3.5-turbo",
                "temperature": 0.7,
                "max_tokens": 1000,
            }
        }


class ChatResponse(BaseModel):
    """聊天响应模型"""

    id: str = Field(..., description="响应ID")
    model: str = Field(..., description="使用的模型")
    message: Message = Field(..., description="助手消息")
    usage: Dict[str, int] = Field(..., description="使用情况")
    created_at: datetime = Field(default_factory=datetime.now)


class EmbeddingRequest(BaseModel):
    """嵌入请求模型"""

    texts: List[str] = Field(..., min_length=1, description="文本列表")
    model: str = Field("text-embedding-ada-002", description="嵌入模型")


class EmbeddingResponse(BaseModel):
    """嵌入响应模型"""

    embeddings: List[List[float]] = Field(..., description="嵌入向量列表")
    model: str = Field(..., description="使用的模型")
    dimensions: int = Field(..., description="向量维度")


class VectorSearchRequest(BaseModel):
    """向量搜索请求模型"""

    query: str = Field(..., description="查询文本")
    top_k: int = Field(5, ge=1, le=100, description="返回结果数量")
    min_score: float = Field(0.0, ge=0.0, le=1.0, description="最小相似度分数")


class VectorSearchResult(BaseModel):
    """向量搜索结果模型"""

    id: str = Field(..., description="文档ID")
    content: str = Field(..., description="文档内容")
    score: float = Field(..., ge=0.0, le=1.0, description="相似度分数")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="元数据")


class VectorSearchResponse(BaseModel):
    """向量搜索响应模型"""

    query: str = Field(..., description="查询文本")
    results: List[VectorSearchResult] = Field(..., description="搜索结果")
    total: int = Field(..., description="总结果数")
