import os

from sqlmodel import create_engine, SQLModel, Session

base_dir = os.path.abspath(os.path.dirname(__file__))
DATABASE_URL = "sqlite:///" + os.path.join(base_dir, "sqlmodel-demo.db")

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
