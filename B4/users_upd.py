import uuid
import datetime

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = sa.Column(sa.INTEGER, primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.REAL)





def request_data():
    first_name = input("first name:")
    last_name = input("last name:")
    email = input("email:")
    gender = input("gender (Male or Female):")
    birthdate = input("birthdate YYYYMMDD:")
    height = float(input("height (sm):"))
    user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        gender=gender,
        birthdate=birthdate,
        height=height
    )
    return user


def connect_db():
    engine = sa.create_engine(DB_PATH)
    session = sessionmaker(engine)
    return session()


def main():
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print('data saved')


if __name__ == '__main__':
    main()
