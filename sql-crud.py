from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

from sqlalchemy.util import deprecations

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


deprecations.SILENCE_UBER_WARNING = True


db = create_engine("postgresql:///chinook")
base = declarative_base()


class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

    
Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

# ada_lovelace = Programmer(
#     first_name="Ada",
#     last_name="Lovelace",
#     gender="f",
#     nationality="British",
#     famous_for="First programmer ever"
# )

# alan_turing = Programmer(
#     first_name="Alan",
#     last_name="Turing",
#     gender="m",
#     nationality="British",
#     famous_for="Modern computing"
# )

# grace_hopper = Programmer(
#     first_name="Grace",
#     last_name="Hopper",
#     gender="f",
#     nationality="American",
#     famous_for="COBOL language"
# )

# margaret_hamilton = Programmer(
#     first_name="Margaret",
#     last_name="Hamilton",
#     gender="f",
#     nationality="American",
#     famous_for="Apollo 11"
# )

# bill_gates = Programmer(
#     first_name="Bill",
#     last_name="Gates",
#     gender="m",
#     nationality="American",
#     famous_for="Microsoft"
# )

# tim_berners_lee = Programmer(
#     first_name="Tim",
#     last_name="Berners-Lee",
#     gender="m",
#     nationality="British",
#     famous_for="World-Wide Web"
# )

jaime_hyland = Programmer(
    first_name="Jaime",
    last_name="Hyland",
    gender="m",
    nationality="Irish",
    famous_for="Language lessons"
)

# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(jaime_hyland)


# programmer =  session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "Best chili con carne maker"

# session.commit()

people = session.query(Programmer)
for person in people:
    if person.gender == "f":
        person.gender = "female"
    elif person.gender == "m":
        person.gender = "male"
    else:
        print("Gender not defined")
    session.commit()

programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender, 
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )