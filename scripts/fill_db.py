from faker import Faker
from sqlalchemy.exc import DBAPIError

from src.users.models import User
from src.users.schemas import GenderType
from src.database import SessionLocal

NUMBER_OF_USERS = 150


def run():
    fake = Faker('ru_RU')
    session = SessionLocal()
    gender_list = list(GenderType)
    users = []
    for _ in range(NUMBER_OF_USERS):
        users.append(User(name=fake.name()[:64],
                          gender=fake.random.choice(gender_list)))
        session.add_all(users)
    try:
        session.commit()
    except DBAPIError as err:
        print("[!] Failed to populate database:", err, sep="\n")
        session.rollback()
    finally:
        print("[*] Script ending")


if __name__ == "__main__":
    run()
