from typing import List
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from database.db_manager import Base, DBManager


class Product(Base):

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

    invoice_id = Column(Integer, ForeignKey('invoices.id'), nullable=False)
    invoice = relationship('Invoice', back_populates='products')


def get_rows(db_path: str) -> List[Product]:
    session = DBManager(db_path=db_path).session
    products = []
    try:
        if session is not None:
            result = session.query(Product).all()
            for item in result:
                products.append(item)
    except Exception as e:
        print(f'Exception occurred: {e}')
    return products

def get_columns() -> List[str]:
    
    return Product.__table__.columns.keys()

def get_products_by_invoice_id(db_path: str, invoice_id: int) -> List[object]:
    """
    Fetch the products from the database
    Args:
        invoice_id (int): Invoice ID
    Returns:
        List[object]: List of database Product objects
    """

    session = DBManager(db_path=db_path).session
    products = []
    try:
        if session is not None:
            result = session.query(Product).filter_by(invoice_id=invoice_id)
            for item in result:
                products.append(item)
    except Exception as e:
        print(f'Exception occurred: {e}')
    return products
