import uuid
import datetime
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime as dt

DB_PATH = "sqlite:///sochi_athletes.sqlite3"


Base = declarative_base()


class Athelete(Base):
    __tablename__ = "athelete"
    id = sa.Column(sa.INTEGER, primary_key=True)
    age = sa.Column(sa.INTEGER)
    birthdate = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    height = sa.Column(sa.REAL)
    name = sa.Column(sa.Text)
    weight = sa.Column(sa.INTEGER)
    gold_medals = sa.Column(sa.INTEGER)
    silver_medals = sa.Column(sa.INTEGER)
    bronze_medals = sa.Column(sa.INTEGER)
    total_medals = sa.Column(sa.INTEGER)
    sport = sa.Column(sa.Text)
    country = sa.Column(sa.Text)
    

def connect_db():
    engine = sa.create_engine(DB_PATH)
    session = sessionmaker(engine)
    return session()


def find_users(user_id, session):
    query_target = session.query(User).filter(User.id == user_id).first()
    if query_target is not None:
        query_total = session.query(User)
        height_dict = {user.id: user.height for user in query_total.all()}
        birthdate_dict = {user.id: user.birthdate for user in query_total.all()}
        closest_by_height = find_closest_by_height(height_dict, user_id)
        closest_by_birthdate = find_closest_by_birthdate(birthdate_dict, user_id)
    else:
        print('no user with this id')


def find_atheletes(user_id, session):
    query_target = session.query(Athelete).filter(Athelete.id == user_id).first()
    if query_target is not None:
        query_total = session.query(Athelete)
        height_dict = {athelete.id: athelete.height for athelete in query_total.all()}
        birthdate_dict = {athelete.id: athelete.birthdate for athelete in query_total.all()}
        closest_by_height = find_closest_by_height(height_dict, user_id)
        name_dict = {athelete.id: athelete.name for athelete in query_total.all()}
        closest_by_birthdate = find_closest_by_birthdate(birthdate_dict, user_id)

        print('original: ')
        print(name_dict[user_id])
        print(birthdate_dict[user_id])
        print(height_dict[user_id])
        print('-----------')

        print('closest by birthday: ')
        print(name_dict[closest_by_birthdate])
        print(birthdate_dict[closest_by_birthdate])
        print('-----------')

        print('closest by height: ')
        print(name_dict[closest_by_height])
        print(height_dict[user_id])
        print('-----------')

    else:
        print('no user with this id')


#todo
def find_closest_by_birthdate(dict, target):
    temp = 0
    etalon = str2date(dict[target])
    delta = 0
    first_item = 0
    for key in dict.keys():
        if key != target and dict[key] != dict[target]:
            first_item = key
            break
    delta = str2date(dict[first_item]) - etalon
    temp = first_item
    for key, value in dict.items():
        if key != target and value is not None and dict[key] != dict[target]:
            foo = str2date(value)
            delta_local = foo - etalon
            if (abs(delta_local.days) < abs(delta.days)):
                delta = delta_local
                temp = key
    return temp


def find_closest_by_height(dict, target):
    temp = None
    first_item = None
    for key in dict.keys():
        if key != target and dict[key] != dict[target]:
            first_item = key
            break
    delta = abs(dict[first_item] - dict[target])


    for key, value in dict.items():
        if key != target and dict[key] is not None and abs((dict[key] - dict[target])) < delta:
            temp = key
            delta = abs((dict[key] - dict[target]))
    return temp


def str2date(value):
    return dt.date(int(value[0:4]), int(value[5:7]), int(value[8:]))


def main():
    user_id = int(input('type athelete id:'))
    session = connect_db()
    find_atheletes(user_id, session)


if __name__ == '__main__':
    main()
