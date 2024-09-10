from sqlalchemy import (
    Column,
    Integer,
    Float,
    ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Product(Base):

    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    price = Column(Float)

    invoice_id = Column(Integer, ForeignKey('invoice.id'), nullable=False)
