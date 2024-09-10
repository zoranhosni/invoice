from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class DBManager:

    def __init__(self, db_path) -> None:
        self.db_path = db_path
        self.engine = None
        self.session = None

    def connect(self):
        self.engine = create_engine(self.db_path)
        Base.metadata.create_all(self.engine)
        session_ = sessionmaker(bind=self.engine)
        self.session = session_()

        return self.session
