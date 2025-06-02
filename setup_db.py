from lib.db.setup import Base, engine
from lib.models.book import Book
from lib.models.user import User
from lib.models.lending import Lending

Base.metadata.create_all(engine)
print("Database tables created/updated successfully.")
