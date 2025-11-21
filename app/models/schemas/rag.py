from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
from app.models.schemas.ai import VectorSearchResult


class RAGQueryRequest(BaseModel):
    """RAG 查询请求模型"""

    query: str = Field(..., min_length=1, description="查询问题")
    top_k: int = Field(5, ge=1, le=20, description="检索文档数量")
    temperature: float = Field(0.7, ge=0.0, le=2.0, description="生成温度")
    max_tokens: Optional[int] = Field(None, ge=1, description="最大生成长度")
    include_contexts: bool = Field(True, description="是否包含上下文")

    class Config:
        schema_extra = {
            "example": {"query": "What is machine learning?", "top_k": 5, "temperature": 0.7, "max_tokens": 1000}
        }


class RAGQueryResponse(BaseModel):
    """RAG 查询响应模型"""

    query: str = Field(..., description="原始查询")
    answer: str = Field(..., description="生成的答案")
    contexts: List[VectorSearchResult] = Field(..., description="检索到的上下文")
    context_count: int = Field(..., description="上下文数量")
    model_used: str = Field(..., description="使用的模型")
    processing_time: float = Field(..., description="处理时间（秒）")
    status: str = Field(..., description="处理状态")

    class Config:
        schema_extra = {
            "example": {
                "query": "What is machine learning?",
                "answer": "Machine learning is a subset of artificial intelligence...",
                "contexts": [
                    {
                        "id": "doc_1",
                        "content": "Machine learning involves algorithms...",
                        "score": 0.95,
                        "metadata": {"source": "textbook"},
                    }
                ],
                "context_count": 1,
                "model_used": "gpt-3.5-turbo",
                "processing_time": 1.23,
                "status": "success",
            }
        }


class Document(BaseModel):
    """文档模型"""

    id: str = Field(..., description="文档ID")
    content: str = Field(..., description="文档内容")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="元数据")
    embedding: Optional[List[float]] = Field(None, description="嵌入向量")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class DocumentCreate(BaseModel):
    """文档创建模型"""

    content: str = Field(..., description="文档内容")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="元数据")


class DocumentUpdate(BaseModel):
    """文档更新模型"""

    content: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class DocumentBatchResponse(BaseModel):
    """文档批量操作响应"""

    success: bool = Field(..., description="操作是否成功")
    processed: int = Field(..., description="处理的文档数量")
    failed: int = Field(0, description="失败的文档数量")
    errors: List[str] = Field(default_factory=list, description="错误信息")
