from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.db.setup import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    lendings = relationship("Lending", back_populates="user")

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"
