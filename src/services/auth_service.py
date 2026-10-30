"""Authentication Service - Business logic for user logins and credentials verification."""

from datetime import datetime, timedelta
import hashlib
from typing import Optional
import jwt

from src.core.config import settings
from src.core.exceptions import AccountInactiveError, InvalidCredentialsError
from src.repositories.user_repository import IUserRepository
from src.schemas.auth import LoginRequest, TokenResponse, UserResponse


class AuthService:
    """Manages staff credential verification and token creation."""

    def __init__(self, user_repo: IUserRepository):
        self._user_repo = user_repo

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    async def authenticate(self, credentials: LoginRequest) -> TokenResponse:
        user = await self._user_repo.get_by_email(credentials.email)
        if not user or user.password_hash != self.hash_password(credentials.password):
            raise InvalidCredentialsError("Invalid email or password")

        if not user.is_active:
            raise AccountInactiveError("User account has been deactivated by Hospital Administrator")

        expires_delta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        expire = datetime.utcnow() + expires_delta
        payload = {
            "sub": str(user.id),
            "email": user.email,
            "role": user.role.value,
            "exp": expire,
        }
        token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

        return TokenResponse(
            access_token=token,
            user=UserResponse.model_validate(user),
        )
