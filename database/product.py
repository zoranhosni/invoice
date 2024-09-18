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
    invoices = []
    try:
        if session is not None:
            result = session.query(Product).all()
            for item in result:
                invoices.append(item)
    except Exception as e:
        print(f'Exception occurred: {e}')
    return invoices

def get_columns(db_path: str) -> List[str]:
    session = DBManager(db_path=db_path).session
    try:
        if session is not None:
            return session.query(Product).column_descriptions
    except Exception as e:
        print(f'Exception occurred: {e}')
    
    return None
