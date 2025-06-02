from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from lib.db.setup import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    is_available = Column(Boolean, default=True)

    lendings = relationship("Lending", back_populates="book")

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}', available={self.is_available})>"


