from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class DBManagerException(Exception):
    """
    Base DB Manager Exception class
    """
    pass


class DBManager:
    """
    DB Manger class

    It's an interface towards the data stored in the database
    """
    def __init__(self, db_path) -> None:
        self.db_path = db_path
        self.engine = None
        self.session = self._connect()

    def _connect(self):
        import database.invoice
        import database.product
        self.engine = create_engine(self.db_path)
        Base.metadata.create_all(self.engine)
        session_ = sessionmaker(bind=self.engine)

        return session_()
    