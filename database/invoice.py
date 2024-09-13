from sqlalchemy import (
    Column,
    Integer,
    DateTime
)
from sqlalchemy.orm import relationship
from database.db_manager import Base


class Invoice(Base):

    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    issue_date = Column(DateTime)

    products = relationship('Product', back_populates='invoice', lazy='dynamic')
