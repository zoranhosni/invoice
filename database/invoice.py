from typing import List
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
)
from sqlalchemy.orm import relationship
from database.db_manager import Base, DBManager


class Invoice(Base):

    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    issue_date = Column(DateTime)

    products = relationship('Product', back_populates='invoice', lazy='dynamic')

def get_rows(db_path: str) -> List[Invoice]:
    session = DBManager(db_path=db_path).session
    invoices = []
    try:
        if session is not None:
            result = session.query(Invoice).all()
            for item in result:
                invoices.append(item)
    except Exception as e:
        print(f'Exception occurred: {e}')
    return invoices

def get_columns() -> List[str]:
    
    return Invoice.__table__.columns.keys()
