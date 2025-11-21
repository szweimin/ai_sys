from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class UserRole(str, Enum):
    """用户角色枚举"""

    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


class UserBase(BaseModel):
    """用户基础模型"""

    email: EmailStr = Field(..., description="用户邮箱")
    username: str = Field(..., min_length=3, max_length=50, description="用户名")
    full_name: Optional[str] = Field(None, description="用户全名")


class UserCreate(UserBase):
    """用户创建模型"""

    password: str = Field(..., min_length=8, description="密码")


class UserUpdate(BaseModel):
    """用户更新模型"""

    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    full_name: Optional[str] = None
    is_active: Optional[bool] = None


class UserInDB(UserBase):
    """数据库中的用户模型"""

    id: str = Field(..., description="用户ID")
    role: UserRole = Field(UserRole.USER, description="用户角色")
    is_active: bool = Field(True, description="是否激活")
    created_at: datetime = Field(..., description="创建时间")
    updated_at: datetime = Field(..., description="更新时间")

    class Config:
        from_attributes = True  # 替换原来的 orm_mode


class UserResponse(UserInDB):
    """用户响应模型"""

    pass


class UserLogin(BaseModel):
    """用户登录模型"""

    email: EmailStr
    password: str = Field(..., min_length=8)


class Token(BaseModel):
    """令牌响应模型"""

    access_token: str
    token_type: str = "bearer"
    expires_in: int = 3600


class TokenData(BaseModel):
    """令牌数据模型"""

    user_id: Optional[str] = None
    email: Optional[str] = None
