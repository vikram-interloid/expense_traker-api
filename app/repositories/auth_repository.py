from app.repositories.base import BaseRepository
from sqlalchemy import select


from app.models.refresh_token import RefreshToken
from app.models.user import User


class AuthRepository(BaseRepository):
    
    def get_user_by_id(self, user_id: int) -> User | None:
        stmt = select(User).where(User.id == user_id)
        return self.db.scalar(stmt)
    
    def get_user_by_email(self, email: str) -> User | None:
        stmt = select(User).where(User.email == email)
        return self.db.scalar(stmt)

    def get_user_by_username(self, username: str) -> User | None:
        stmt = select(User).where(User.username == username)
        return self.db.scalar(stmt)

    def create_user(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def create_refresh_token(
        self,
        refresh_token: RefreshToken,
    ) -> RefreshToken:
        self.db.add(refresh_token)
        self.db.commit()
        self.db.refresh(refresh_token)
        return refresh_token

    def get_refresh_token(
        self, 
        token: str
    ) -> RefreshToken | None:
        stmt = select(RefreshToken).where(
            RefreshToken.token == token,
            RefreshToken.is_revoked.is_(False),
        )
        return self.db.scalar(stmt)
    
    def revoke_refresh_token(
    self,
    token: str,
    ) -> bool:
        refresh_token = self.get_refresh_token(token)
        if refresh_token is None:
            return False
        refresh_token.is_revoked = True
        self.db.commit()
        self.db.refresh(refresh_token)
        return True


