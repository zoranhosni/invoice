from sqlalchemy import (
    Column,
    Integer,
    DateTime
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    relationship,
    backref,
)


Base = declarative_base()


class Invoice(Base):

    __tablename__ = 'invoice'

    id = Column(Integer, primary_key=True)
    issue_date = Column(DateTime)

    products = relationship('Product', backref=backref('invoice'))
