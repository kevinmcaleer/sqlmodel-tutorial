from models import SQLModel, Hero
from sqlmodel import create_engine, Session


sqlite_file_name = "database.db"  
sqlite_url = f"sqlite:///{sqlite_file_name}"  

engine = create_engine(sqlite_url, echo=True)  


def create_db_and_tables():  
    SQLModel.metadata.create_all(engine)  

def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    session = Session(engine)

    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)

    session.commit()