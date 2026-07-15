from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User


def seed_users(db: Session) -> list[User]:

    users = [
        User(
            username="amal",
            email="amal@example.com",
            password_hash=hash_password("Password@123"),
        ),
        User(
            username="arun",
            email="arun@example.com",
            password_hash=hash_password("Password@123"),
        ),
        User(
            username="vikram",
            email="vikram@example.com",
            password_hash=hash_password("Password@123"),
        ),
        User(
            username="karthik",
            email="karthik@example.com",
            password_hash=hash_password("Password@123"),
        ),
        User(
            username="rahul",
            email="rahul@example.com",
            password_hash=hash_password("Password@123"),
        ),
        User(
            username="priya",
            email="priya@example.com",
            password_hash=hash_password("Password@123"),
        ),
        User(
            username="anitha",
            email="anitha@example.com",
            password_hash=hash_password("Password@123"),
        ),
        User(
            username="sanjay",
            email="sanjay@example.com",
            password_hash=hash_password("Password@123"),
        ),
        User(
            username="deepak",
            email="deepak@example.com",
            password_hash=hash_password("Password@123"),
        ),
        User(
            username="meena",
            email="meena@example.com",
            password_hash=hash_password("Password@123"),
        ),
    ]

    db.add_all(users)
    db.commit()

    for user in users:
        db.refresh(user)

    print("10 users seeded successfully.")

    return users