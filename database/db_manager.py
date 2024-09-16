from typing import List
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

    def get_invoices(self) -> List:
        """
        Fetch all invoices from the database

        Returns:
            List[Invoice]: List of Invoice objects
        """
        from database.invoice import Invoice
        invoices = []
        try:
            if self.session is not None:
                result = self.session.query(Invoice).all()
                for item in result:
                    invoices.append(item)
        except Exception as e:
            print(f'Exception occurred: {e}')
        
        return invoices
    
    def get_products(self) -> List:
        """
        Fetch all products from the database

        Returns:
            List[Product]: List of Product objects
        """
        from database.product import Product
        products = []
        try:
            if self.session is not None:
                result = self.session.query(Product).all()
                for item in result:
                    products.append(item)
        except Exception as e:
            print(f'Exception occurred: {e}')
        
        return products
    