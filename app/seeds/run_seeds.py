from app.db.session import SessionLocal

from app.seeds.seed_users import seed_users
from app.seeds.seed_categories import seed_categories
from app.seeds.seed_transactions import seed_transactions

def run():

    db = SessionLocal()

    try:
        users = seed_users(db)

        seed_categories(
            db,
            users,
        )

        seed_transactions(
            db,
            users,
        )

    finally:
        db.close()

if __name__ == "__main__":
    run()
