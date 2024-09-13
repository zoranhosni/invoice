from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey
)
from sqlalchemy.orm import relationship
from database.db_manager import Base


class Product(Base):

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

    invoice_id = Column(Integer, ForeignKey('invoices.id'), nullable=False)
    invoice = relationship('Invoice', back_populates='products')
