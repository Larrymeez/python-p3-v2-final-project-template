from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from lib.db.setup import Base

class Lending(Base):
    __tablename__ = 'lendings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    book_id = Column(Integer, ForeignKey('books.id'))
    borrowed_date = Column(DateTime, default=datetime.utcnow)
    returned_date = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="lendings")
    book = relationship("Book", back_populates="lendings")


